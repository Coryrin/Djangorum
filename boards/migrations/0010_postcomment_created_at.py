# Generated by Django 2.0.7 on 2019-01-26 12:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0009_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
