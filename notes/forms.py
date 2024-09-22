from django import forms 

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=('title_Name', 'textt', 'description')

    def clean_title_Name(self):
        title_Name= self.cleaned_data.get('title_Name')
        if 'Django' not in title_Name:
            raise forms.ValidationError("we only accept notes about Django")
        return title_Name
