# Generated by Django 3.2.20 on 2023-09-14 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='term',
            old_name='creation_date',
            new_name='timestamp',
        ),
    ]
