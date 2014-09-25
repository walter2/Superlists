#!/user/bin/python3

from django import forms

from lists.models import Item

EMPTY_LIST_ERROR = "You cannot have an empty list item"

class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'autofocus': 'true',
                'class': 'form-control input-lg',
            }),
        }
        error_messages = {
            'text': {'required': EMPTY_LIST_ERROR}
        }


