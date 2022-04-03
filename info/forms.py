from info.models import Documents
from django import forms

class DocumetsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ('doc','name')
