from django.db import models
from django.utils import timezone


class AbstractPerson(models.Model):
    name = models.CharField(max_length=30, unique=True)
    birth_date = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        abstract = True

    def get_age(self):
        today = timezone.now().date()
        return today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day))


class Employee(AbstractPerson):
    position = models.CharField(max_length=30)
    salary = models.CharField(max_length=30)
    work_experience = models.CharField(max_length=30, verbose_name='Work experience since some year')

    def save(self, *args, **kwargs):
        print(f'Saving Employee with name {self.name}, position {self.position}, salary {self.salary}, '
              f'work_experience {self.work_experience}')
        super().save(*args, **kwargs)


class Passport(Employee):
    inn = models.IntegerField(max_length=14, verbose_name='INN PASSPORT')
    id_card = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='Number_id_passport')

    def get_gender(self):
        if self.inn[0] in ['1', '3', '5', '7', '9']:
            return "Female"
        else:
            return "Male"

    def save(self, *args, **kwargs):
        print(f'Saving Passport for Employee {self.employee.name} with inn {self.inn}, id_card {self.id_card}')
        super().save(*args, **kwargs)


class WorkProjects(models.Model):
    members = models.ManyToManyField(Employee, related_name='groups', through="Membership")
    project_name = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        print(f'Saving WorkProject with project_name {self.project_name}')
        super().save(*args, **kwargs)


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_project = models.ForeignKey(WorkProjects, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def save(self, *args, **kwargs):
        print(f'Saving Membership for Employee {self.employee.name} and WorkProject {self.work_project.project_name} '
              f'with date_joined {self.date_joined}')
        super().save(*args, **kwargs)


class Client(AbstractPerson):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        print(f'Saving Client with name {self.name}, address {self.address}, phone_number {self.phone_number}')
        super().save(*args, **kwargs)


class VIPClient(Client):
    vip_status_start = models.DateField()
    donation_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'vip_clients'




