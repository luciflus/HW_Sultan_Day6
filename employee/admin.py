from django.contrib import admin

from .models import AbstractPerson, Employee, Passport, WorkProject, Membership, Client, VIPClient

admin.site.register(Employee)
admin.site.register(Passport)
admin.site.register(WorkProject)
admin.site.register(Membership)
admin.site.register(Client)
admin.site.register(VIPClient)
