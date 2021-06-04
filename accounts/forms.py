from django import forms

from accounts.models import Files


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('title', 'pdf',)