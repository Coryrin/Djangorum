# Generated by Django 2.0.7 on 2019-01-31 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0013_auto_20190129_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_html',
            field=models.TextField(blank=True, default=''),
        ),
    ]
