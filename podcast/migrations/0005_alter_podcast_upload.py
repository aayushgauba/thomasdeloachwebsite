# Generated by Django 4.1 on 2022-09-18 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0004_alter_podcast_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='upload',
            field=models.FileField(upload_to='podcasts/'),
        ),
    ]
