# Generated by Django 3.2.6 on 2021-08-30 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0020_rename_ordervideo_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('artist', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='audios/%y')),
                ('audio_link', models.CharField(blank=True, max_length=200, null=True)),
                ('duration', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
