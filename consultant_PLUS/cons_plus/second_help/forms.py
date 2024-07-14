from django import forms
from .models import Tag


class TagSearchForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)