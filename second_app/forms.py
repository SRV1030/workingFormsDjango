from django import forms
from second_app.models import details

class Fn(forms.ModelForm):

    class Meta():
        model = details
        fields = '__all__'
