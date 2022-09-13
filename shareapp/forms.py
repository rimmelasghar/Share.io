from django import forms
from .models import Files
class UploadFileForm(forms.Form):
    file = forms.FileField(label='subject')

    
    class Meta:
        model = Files
        fields = ['file']
