# Generated by Django 3.1.3 on 2021-04-22 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tool',
            old_name='created_at',
            new_name='created_date',
        ),
    ]
