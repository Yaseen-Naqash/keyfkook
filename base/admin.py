from django.contrib import admin
from .models import Topic, Item
# Register your models here.



@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):


    search_fields = (
        'title', 
    )


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    list_display = ('title','price' , 'topic', 'visiable',)


    search_fields = (
        'title', 
    )

    list_filter = (
        'topic',

    )