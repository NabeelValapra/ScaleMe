import pytest
from .factories import AddressBookFactory, UserFactory
from django.contrib.auth.models import User
from optimj.forms import AddressBookForm


@pytest.mark.django_db
def test_addressbook():
    addressOne = AddressBookFactory(first_name='Nabeel')
    assert addressOne.first_name == 'Nabeel'
   
    for name in ['Sabir', 'Anas', 'Thameem', 'Riyas']:
        user = UserFactory()
        address = AddressBookFactory(first_name=name)
        address.phone = 123
        address.created_by = user
        address_form = AddressBookForm(instance=address)
        assert address_form.is_valid() == True
        assert address.email == 'nabeelvalapra@gmail.com'
        assert address.created_by == user

