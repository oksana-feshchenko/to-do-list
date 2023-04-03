from django import forms

from list.models import Task


class TaskCreateForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.SelectDateWidget())

    class Meta:
        model = Task
        fields = "__all__"
