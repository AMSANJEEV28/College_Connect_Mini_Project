from django import forms
from .models import Group

class GroupCreationForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']

class GroupSearchForm(forms.Form):
    search_query = forms.CharField(label='Search Group')

class GroupJoinForm(forms.Form):
    group_id = forms.CharField(label='Group ID')
