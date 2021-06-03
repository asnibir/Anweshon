from django import forms

class SearchForm(forms.Form):
    query_key = forms.CharField(max_length=500)