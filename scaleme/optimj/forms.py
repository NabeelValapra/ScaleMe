from django import forms
from models import AddressBook


class AddressBookForm(forms.ModelForm):

    class Meta:
        model = AddressBook
        fields = '__all__'
