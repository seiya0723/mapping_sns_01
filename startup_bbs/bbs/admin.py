from django.contrib import admin

from .models import Topic
# Register your models here.

class TopicAdmin(admin.ModelAdmin):

    list_display = ["name","dt","comment","approval"]
    search_fields = ["comment"]

    list_editable = ["approval"]


admin.site.register(Topic,TopicAdmin)