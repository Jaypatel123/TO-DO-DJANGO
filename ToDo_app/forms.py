from django.contrib.auth.models import User

from django.forms import ModelForm
from .models import *

class Todo(ModelForm):
    class Meta:
        model = Task
        fields = ['title']
        lables = {'title': 'Title'}