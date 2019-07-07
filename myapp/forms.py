from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='select files',
        help_text='',
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )