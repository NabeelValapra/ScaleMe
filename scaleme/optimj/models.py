from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class AddressBook(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='First Name')
    last_name = models.CharField(max_length=20, verbose_name='Last Name')
    phone = models.IntegerField(verbose_name='Phone no')
    email = models.EmailField(verbose_name='Email ID')
    address = models.TextField(verbose_name='Address')
    created_by = models.ForeignKey(User)

    class Meta:
        db_table = 'scaleme_optimj'


