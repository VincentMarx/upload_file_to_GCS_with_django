from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='',
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )