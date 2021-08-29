from django.contrib import admin
from django.db.models.query_utils import select_related_descend
from .models import *
# Register your models here.
class Post(admin.ModelAdmin):
    list_display = ['linkfb','linktwitter','phone']
    search_fields = ['id']
#class link
admin.site.register(link,Post)
#class hero
admin.site.register(hero)
#class about 
admin.site.register(about)
#class process
admin.site.register(process)
#class team
class Post_team(admin.ModelAdmin):
    list_display = ['name','position']
admin.site.register(team,Post_team)
#class solutions
admin.site.register(solutions)
#class possibilities
admin.site.register(possibilities)
#class services
admin.site.register(services)
#class footer
admin.site.register(footer)