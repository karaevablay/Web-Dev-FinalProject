from django.contrib import admin
from django.contrib.admin import ModelAdmin
from api.models import Project, Blog


# Register your models here.


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ('id', 'author', 'title',)
    search_fields = ('author', 'title')
    ordering = ('id',)


@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ('id', 'author', 'title',)
