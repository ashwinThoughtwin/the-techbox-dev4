# Generated by Django 3.1.3 on 2021-04-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20210423_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
