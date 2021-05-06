# Generated by Django 3.1.3 on 2021-04-23 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20210423_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowTool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign_on', models.DateTimeField()),
                ('expire_on', models.DateTimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.employee')),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.tool')),
            ],
        ),
    ]
