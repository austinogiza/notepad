# Generated by Django 2.2.10 on 2020-06-12 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200612_1641'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='todo',
            unique_together=set(),
        ),
    ]
