from django import forms
from .models import Files
class UploadFileForm(forms.Form):
    file = forms.FileField()

    
    class Meta:
        model = Files
        fields = ['file']
