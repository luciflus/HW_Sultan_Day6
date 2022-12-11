from employee.models import Client, Employee, Membership, Passport, VIPClient, WorkProject
from django.db.models import Q, Subquery

#Создание 4-x Emloyee (с какими то данными, одним из них должны быть Вы. То есть ввести свои данные)
# e1 = Employee.objects.create(name='Sultan Usmanov', birth_date='1987-06-05', position='DevOps', salary='10000', work_experience=2018)
# e2 = Employee.objects.create(name='Ivan Ivanov', birth_date='1990-06-05', position='Python Developer', salary='11000', work_experience=2015)
# e3 = Employee.objects.create(name='Petr Petrov', birth_date='1991-06-05', position='Java Developer', salary='12000', work_experience=2016)
# e4 = Employee.objects.create(name='Sidor Sidorov', birth_date='1992-06-05', position='GO Developer', salary='13000', work_experience=2017)
# e5 = Employee.objects.create(name='Alen Petrova', birth_date='1992-06-05', position='GO Developer', salary='13000', work_experience=2017)
#
# #Добавление им паспортных данных (себе можно вписать НЕ настоящие паспортные данные)
# inn_e1 = Passport.objects.create(inn=205019870605, id_card='AN2050', employee=e1)
# inn_e2 = Passport.objects.create(inn=205019900605, id_card='AN2050', employee=e2)
# inn_e3 = Passport.objects.create(inn=205019910605, id_card='AN2050', employee=e3)
# inn_e4 = Passport.objects.create(inn=205019920605, id_card='AN2050', employee=e4)
# inn_e5 = Passport.objects.create(inn=105019920605, id_card='AN2050', employee=e5)
#

#Удаление последней записи паспортных данных, и сотрудника
# print(Passport.objects.values('employee__name', 'inn', 'id_card').last())
# a = Passport.objects.values('employee__name', 'inn', 'id_card').last()
# for k, v in a.items():
#     if k == 'employee__name':
#         Employee.objects.get(name=v).delete()

#Создание WorkProject
# wp = WorkProject.objects.create(project_name='Pinterest')

#Добавление в WorkProject всех созданных сотрудников одной датой.
# members = wp.members.set([e1, e2, e3, e4], through_defaults={'date_joined': '2022-12-10'})

#Удаление одного из сотрудников
#Employee.objects.get(pk=33).delete()

#Создание новых клиентов (3 чел)
# c1 = Client.objects.create(name='Petr Petrov', birth_date='1987-06-05', address='Chuy str 126 ', phone_number='+996771505050')
# c2 = Client.objects.create(name='Ivan Ivanov', birth_date='1988-06-05', address='Chuy str 126 ', phone_number='+996771505051')
# c3 = Client.objects.create(name='Sidor Sidorov', birth_date='1989-06-05', address='Chuy str 126 ', phone_number='+996771505052')

#Создание нового VIP клиента (1 чел)
# vip_c1 = VIPClient.objects.create(vip_status_start='2022-11-10', donation_amount=5000, client=c1)

#Удаление одного из обычных клиентов
#Client.objects.get(pk=3).delete()

# Вывести в окно терминала список всех Employee
# print(f'Employees - {Employee.objects.all()}')
#
# # Вывести в окно терминала список всех Employee с паспортными данными
# print(Passport.objects.values('employee__name', 'inn', 'id_card'))
#
# # Вывести в окно терминала все проекты
# print(f'Projects - {WorkProject.objects.all()}')
#
# # Вывести в окно терминала проекты в которых трудитесь Вы, точнее Employee которого Вы создали используя свои личные данные
# print(WorkProject.objects.filter(members__name='Sultan Usmanov'))
#
# # Вывести всех Клиентов
# print(f'Clients - {Client.objects.all()}')

# # Вывести Всех ВИП Клиентов
# print(f'VIP - {VIPClient.objects.all()}')


