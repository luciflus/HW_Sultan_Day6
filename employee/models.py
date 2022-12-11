from django.db import models
from datetime import date, time, datetime, timedelta
import datetime

class AbstractPerson(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField()

    def get_age(self):
        dateresult = datetime.datetime.strptime(self.birth_date, '%Y-%m-%d')
        age = datetime.datetime.today().year - dateresult.year
        return (f'Fullname - {self.name} {age}')

    def __str__(self):
        return f'{self.name} - {self.get_age()}'

    class Meta:
        abstract = True
        ordering = ['name', ]

class Employee(AbstractPerson):
    position = models.CharField(max_length=20)
    salary = models.IntegerField()
    work_experience = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta(AbstractPerson.Meta):
        pass

class Passport(models.Model):
    inn = models.IntegerField()
    id_card = models.CharField(max_length=20)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def get_gender(self):
        inn_1 = str(self.inn)
        if inn_1[0] == '1':
            result = 'Female'
        elif inn_1[0] == '2':
            result = 'Male'
        return result

    def save(self, *args, **kwargs):
        print(f'inn - {self.inn}, id_card - {self.id_card}, employee - {self.employee}, {self.get_gender()}')
        super().save(*args, **kwargs)

class WorkProject(models.Model):
    project_name = models.CharField(max_length=20)
    members = models.ManyToManyField(Employee, related_name='projects', through='Membership')

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        print(f'project_name - {self.project_name}')
        super().save(*args, **kwargs)

class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    workproject = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def __str__(self):
         return f'{self.workproject.project_name} - {self.employee.name}'

    def save(self, *args, **kwargs):
        print(f'employee - {self.employee}, workproject - {self.workproject}, date_joined - {self.date_joined}')
        super().save(*args, **kwargs)

class Client(AbstractPerson):
    address = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return f'{self.name} - {self.address}'

class VIPClient(models.Model):
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField()
    client = models.OneToOneField(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.vip_status_start

    def save(self, *args, **kwargs):
        print(f'vip_status_start - {self.vip_status_start}, donation_amount - {self.donation_amount}, client - {self.client}')
        super().save(*args, **kwargs)