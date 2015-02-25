from django.db import models


# Create your models here.
class Blog(models.Model):
    owner = models.ForeignKey('auth.User', related_name='blogs', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    likes = models.IntegerField()
    comment = models.CharField(max_length=200)

    class Meta:
        db_table = 'scaleme_blogs'

