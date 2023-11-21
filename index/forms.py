from django import forms
from .models import ToDoModel

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoModel
        fields = ['content', 'deadline']