# Generated by Django 3.2 on 2022-12-10 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
                ('position', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('work_experience', models.DateField()),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VIPClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vip_status_start', models.DateField()),
                ('donation_amount', models.IntegerField()),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.client')),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.IntegerField()),
                ('id_card', models.CharField(max_length=20)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('workproject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.workproject')),
            ],
        ),
    ]