from django.contrib import admin
from django.db.models.query_utils import select_related_descend
from .models import *
# Register your models here.
# class Post(admin.ModelAdmin):
#     list_display = ['linkfb','linktwitter','phone']
#     search_fields = ['id']
# ]
class ReviewInline(admin.TabularInline):
    model = Blog

class Group(admin.ModelAdmin):
    inlines = [ReviewInline]
    search_fields = ['id']
class blog(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Blog,blog)
class author(admin.ModelAdmin):
    list_display = ['email']
admin.site.register(Author,author)
class entry(admin.ModelAdmin):
    list_display = ['headline']
    search_fields = ['blog']
admin.site.register(Entry,entry)