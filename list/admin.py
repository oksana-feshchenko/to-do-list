from django.contrib import admin
from django.contrib.auth.models import Group

from list.models import Task, Tag

admin.site.unregister(Group)


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ["content", "created_at", "deadline", "completed"]
    list_filter = ["content"]
    search_fields = ["title"]


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

