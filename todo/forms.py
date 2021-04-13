from django import forms
from todo.models import NotCompletedTasks


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = NotCompletedTasks
        fields = ['name', 'priority']
