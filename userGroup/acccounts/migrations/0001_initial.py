# Generated by Django 3.0.5 on 2020-04-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.PositiveSmallIntegerField(default=0, help_text='id number for group', primary_key=True, serialize=False, verbose_name='Group number')),
                ('name', models.CharField(max_length=25, verbose_name='Group name')),
                ('descripion', models.TextField(verbose_name='A short description of the group')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=25, verbose_name='User nickname')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='User created date')),
                ('group', models.ManyToManyField(to='acccounts.Group', verbose_name='Groups')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
