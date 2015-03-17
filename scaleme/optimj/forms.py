from django import forms
from models import AddressBook


class AddressBookForm(forms.ModelForm):

    class Meta:
        model = AddressBook
        fields = '__all__'
    
    # def clean_phone(self):
    #     num = self.cleaned_data['phone']
    #     if num != '123':
    #         raise forms.ValidationError("Your test a clean is Successfull. !!!")
        
    #     return num

