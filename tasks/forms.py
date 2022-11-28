from django.forms import ModelForm
from .models import Task

class CreateTaskForm(ModelForm):
    class Meta:
        #en que modelo estará basado
        model = Task
        fields = ['title', 'description', 'priority']

        #widgets = {
        #    'title': forms.TextInput(attrs={'class': 'form-control'}),
        #}