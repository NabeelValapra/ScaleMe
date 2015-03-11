from django.db import models

class AddressBook(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    phone = models.IntegerField(verbose_name='Phone no')
    address = models.TextField(verbose_name='Address')

    class Meta:
        db_table = 'scaleme_optimj'


