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
class Post_hero(admin.ModelAdmin):
    list_display = ['id','title','content']
admin.site.register(hero,Post_hero)
#class about 
class Post_about(admin.ModelAdmin):
    list_display = ['id','about_title','about_content']
admin.site.register(about,Post_about)

#class process
class Post_process(admin.ModelAdmin):
    list_display = ['id','process_title','process_content']
admin.site.register(process,Post_process)

#class team
class Post_team(admin.ModelAdmin):
    list_display = ['id','name','position']
admin.site.register(team,Post_team)

#class solutions
class Post_solution(admin.ModelAdmin):
    list_display = ['id','solutions_title','solutions_main_title','solutions_content']
admin.site.register(solutions,Post_solution)

#class possibilities
class Post_possibilities(admin.ModelAdmin):
    list_display = ['id','possibilities_title','possibilities_main_title','possibilities_content']
admin.site.register(possibilities,Post_possibilities)
#class services
class Post_services(admin.ModelAdmin):
    list_display = ['id','services_title','services_main_title']
admin.site.register(services,Post_services)
#class footer
class Post_footer(admin.ModelAdmin):
    list_display = ['id','footer_content_into','footer_title_tw']
admin.site.register(footer,Post_footer)