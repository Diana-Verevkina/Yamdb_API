# Generated by Django 2.2.16 on 2022-11-02 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Titles',
            new_name='Title',
        ),
    ]