# Generated by Django 3.2.6 on 2021-08-30 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0021_song'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Song',
            new_name='Audio',
        ),
    ]