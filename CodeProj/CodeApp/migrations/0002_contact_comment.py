# Generated by Django 2.0.6 on 2019-03-07 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='comment',
            field=models.TextField(default='', max_length=50000000000),
        ),
    ]
