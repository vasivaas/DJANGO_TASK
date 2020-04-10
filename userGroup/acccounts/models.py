from django.db import models
from django.urls import reverse

# Create your models here.
class Group(models.Model):
    """
    Model for group
    """
    id = models.PositiveSmallIntegerField('Group number', default=0, primary_key=True, help_text='id number for group')
    name = models.CharField('Group name', max_length=25)
    descripion = models.TextField('A short description of the group')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular user instance.
        """
        return reverse('group_info', args=[str(self.id)])

    class Meta:
        verbose_name='Group'
        verbose_name_plural='Groups'
        #ordering=['id']


class User(models.Model):
    """
    Model for user
    """
    nickname = models.CharField('User nickname', max_length=25)
    created_date = models.DateTimeField('User created date', auto_now_add=True, null=True)
    group = models.ManyToManyField(Group, verbose_name='Groups')


    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        """
        Returns the url to access a particular group instance.
        """
        return reverse('user_info', args=[str(self.id)])

    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'




