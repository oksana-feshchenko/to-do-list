from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from list.models import Task, Tag


def index(request):
    task_list = Task.objects.all()
    context = {
        "task_list": task_list,
    }

    return render(request, "list/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("taxi:manufacturer-list")
