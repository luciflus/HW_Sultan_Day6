# Generated by Django 3.2 on 2022-12-10 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='work_experience',
            field=models.CharField(max_length=20),
        ),
    ]
