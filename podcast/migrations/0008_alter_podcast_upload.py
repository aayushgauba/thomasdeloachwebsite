# Generated by Django 4.1 on 2022-09-19 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0007_alter_podcast_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='upload',
            field=models.FileField(upload_to='podcasts'),
        ),
    ]