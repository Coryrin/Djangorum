# Generated by Django 2.0.7 on 2018-11-18 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_auto_20181117_1901'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forumboard',
            options={'verbose_name_plural': 'Forums'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='postcomment',
            options={'verbose_name_plural': 'Thread Replies'},
        ),
    ]
