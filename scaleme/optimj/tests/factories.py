import factory
from optimj.models import AddressBook
from django.contrib.auth.models import User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: '%d-User' % n)
    email = factory.LazyAttribute(lambda obj: '%s@mailinator.com' % obj.username)
    

class AddressBookFactory(factory.Factory):
    FACTORY_FOR = AddressBook
    
    first_name = factory.Sequence(lambda n: '%d_addressUser' % n)
    last_name = 'Valapra'
    email = 'nabeelvalapra@gmail.com'
    phone = 8606771397
    address = 'Valapra House, Morayur PO, Malappuram DIST'
    created_by = factory.SubFactory(UserFactory) 
