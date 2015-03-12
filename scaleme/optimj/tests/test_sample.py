import pytest
from .factories import AddressBookFactory


@pytest.mark.django_db
def test_addressbook():
    addressOne = AddressBookFactory(first_name='Nabeel')
    assert addressOne.first_name == 'Nabeel'
   
    for name in ['Sabir', 'Anas', 'Thameem', 'Riyas']:
        address = AddressBookFactory(first_name=name)
        assert address.email == 'nabeelvalapra@gmail.com'
        assert address.created_by == 'nabeel'
