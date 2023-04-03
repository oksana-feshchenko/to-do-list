from django import forms

from list.models import Task, Tag


class TaskCreateForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.SelectDateWidget())
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Task
        fields = "__all__"
