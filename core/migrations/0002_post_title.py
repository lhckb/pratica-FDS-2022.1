# Generated by Django 4.0.4 on 2022-05-23 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Post title', max_length=100),
        ),
    ]
