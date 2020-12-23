from django import forms
from newapp.models import Ram
class frm(forms.ModelForm):
    class Meta:
        model = Ram
     
        fields = "__all__"