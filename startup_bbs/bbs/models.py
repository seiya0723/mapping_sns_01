from django.db import models
from django.utils import timezone

#models.Modelを継承して、モデルクラスを作る
class Topic(models.Model):

    # 主キー
    #id = models.BigAutoField(primary_key=True)

    #これまで投稿された物に関しては、マイグレーションされた時刻が自動的に入る (そのため、最初からこのフィールドを追加しておいたほうが良い)
    dt      = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)
    name    = models.CharField(verbose_name="名前",max_length=100)
    # 文字列型で2000文字、入力必須
    comment = models.CharField(verbose_name="コメント",max_length=2000)

    #TODO:ここに画像のフィールドを追加する
    image   = models.ImageField(verbose_name="画像",upload_to="bbs/topic/image/",null=True,blank=True)

    #TODO:トピックの承認・未承認を記録するBooleanFieldを追加する
    approval = models.BooleanField(verbose_name="承認",default=False)


    def __str__(self):
        return self.comment