from django.contrib import admin

# Register your models here.
from api.models import *

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'title', 'brief_info', 'link')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'photo', 'brief_info')


@admin.register(MemberInfo)
class MemberInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'about', 'education', 'skills', 'hobbies', 'github', 'tg')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creation_date', 'content')

