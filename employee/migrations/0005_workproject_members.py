# Generated by Django 3.2 on 2022-12-10 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_passport_inn'),
    ]

    operations = [
        migrations.AddField(
            model_name='workproject',
            name='members',
            field=models.ManyToManyField(related_name='groups', through='employee.Membership', to='employee.Employee'),
        ),
    ]