from django.shortcuts import render,redirect
from django.views import View

from django.db.models import Q

from .models import Topic
from .forms import TopicForm

from django.core.paginator import Paginator


# ()内にあるものは継承する親クラス、IndexViewは子クラス
class IndexView(View):

    # selfを使って複雑な計算をGET,POSTそれぞれから呼び出しできる
    #トピックに投稿されたコメントの文字数の合計を計算して返す
    def total_comment(self,topics):
        total   = 0
        for topic in topics:
            total += len(topic.comment)

        return total

    def get(self, request, *args, **kwargs):

        context = {}
        query   = Q()

        if "search" in request.GET:
            print(request.GET["search"])
            #TODO:検索機能を実装させる
            #クエリ=DBに対して検索処理を実行する(動詞)。検索の条件(名詞)

            #指定した単語の完全一致
            #topics  = Topic.objects.filter(comment=request.GET["search"])

            #これではスペース区切りで検索できていない。(スペースも文字列の一部として捉えられる。)
            #topics  = Topic.objects.filter(comment__icontains=request.GET["search"])

            # 『"Django　教科書 入門"』→『"Django 教科書 入門"』→『[ "Django","教科書","入門" ]』
            # 『"Django　　教科書 入門"』→『"Django  教科書 入門"』→『[ "Django","","教科書","入門" ]』→『[ "Django","教科書","入門" ]』
            search      = request.GET["search"]
            raw_words   = search.replace("　"," ").split(" ")

            #words       = [ w for w in raw_words if w != "" ]
            #↑と↓は等価。↑はリスト内包表記
            words = []
            for raw_word in raw_words:
                if raw_word != "":
                    words.append(raw_word)

            for word in words:
                query &= Q(comment__icontains=word)


        #並び替えをして警告を消す
        topics      = Topic.objects.filter(query).order_by("-dt")
        paginator   = Paginator(topics,5)


        """
        # ?page=2 などの指定がある場合、
        if "page" in request.GET:
            context["topics"] = paginator.get_page(request.GET["page"])
        else:
            context["topics"] = paginator.get_page(1)
        """

        # 更に短くかける
        page    = 1
        if "page" in request.GET:
            page    = request.GET["page"]

        context["topics"] = paginator.get_page(page)

        #print(self.total_comment(topics),"文字投稿されました")


        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):
        """
        #request.POST は書き換えできない(requestはイミュータブルなオブジェクト)
        print(request.POST) #POSTリクエストによって送信された全データを表示、辞書型
        print(request.POST["comment"]) #その中からname="comment"のデータを取り出す
        """

        #request.POSTの全データを引数としてフォームオブジェクトを作る
        form    = TopicForm(request.POST,request.FILES)

        #もし、バリデーションルールに則っていればTrue。違反していればFalseが返却される
        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print("バリデーションNG")
            print(form.errors)


        """
        # 受け取ったデータを引数として、commentフィールドに格納し、モデルオブジェクト(posted) を作る
        posted = Topic( comment=request.POST["comment"] )
        # saveメソッドを実行してDBに保存する
        posted.save()
        """

        """
        posted  = Topic()
        posted.comment = request.POST["comment"]
        posted.save()
        """

        """
        topics = Topic.objects.all()
        context = { "topics":topics }

        return render(request,"bbs/index.html",context)
        """
        #POSTメソッドは基本的にはレンダリングではなく、リダイレクトをするのが一般的(更新ボタンを押すと同じ内容の投稿ができてしまう)
        #リダイレクトとは指定したページへジャンプ(直接アクセス)する。GETメソッドになる。

        return redirect("bbs:index")


index   = IndexView.as_view()

"""
def index(request):
    
    return render(request,"bbs/index.html",context)
"""

