from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Write your first name here',
        })
    
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
        )


    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if len(first_name) == 1:
            message = ValidationError(
                'The first name cannot have only one character',
                code='invalid'
            )
            self.add_error('first_name', message)
            
        if first_name == last_name:
            message = ValidationError(
                'The first and last name not be same',
                code='invalid'
            )
            self.add_error('last_name', message)
        
        return super().clean()

    
    """ def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if len(first_name) == 1:
            self.add_error(
                'first_name',
                ValidationError(
                    'Invalid Name',
                    code='invalid'
                )
            )
            
        return first_name """
    