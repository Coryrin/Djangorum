# Generated by Django 2.0.7 on 2018-11-17 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_auto_20180723_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='forum',
        ),
    ]
