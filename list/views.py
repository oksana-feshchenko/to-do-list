from django.shortcuts import render

from list.models import Task


def index(request):
    task_list = Task.objects.all()
    context = {
        "task_list": task_list,
    }

    return render(request, "list/index.html", context=context)
