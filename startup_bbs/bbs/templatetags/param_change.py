from django import template
register = template.Library()

#デコレーター(すぐ下に書いた関数に機能を追加する。今回はテンプレートタグとして呼び出しできる機能)
@register.simple_tag()
def url_replace(request, key, value):
    copied      = request.GET.copy() # {"search":a}
    copied[key] = value # {"search":a,"page":2 }
    return copied.urlencode() # search=a&page=2

"""
このurl_replaceテンプレートタグの呼び出し方
{% url_replace request key value %}
"""