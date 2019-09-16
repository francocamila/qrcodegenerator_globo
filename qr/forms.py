from django import forms
from .models import Post
 

class ExpenseForm(forms.Form):
    CHOICES = (
        ('G1', 'G1'),
        ('GE', 'Globo Esporte'),
    )
    category = forms.ChoiceField(choices=CHOICES)

class PostForm(forms.ModelForm):    

    class Meta:
        model = Post
        fields = ['url']