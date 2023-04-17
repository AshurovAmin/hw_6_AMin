from app.models import *

emp = Employee.objects.create(position='develop js', salary=10000, work_experience='3 years')
emp1 = Employee.objects.create(position='develop python', salary=150000, work_experience='0.3 years')
emp2 = Employee.objects.create(position='develop java', salary=13000, work_experience='3 years')
emp3 = Employee.objects.create(position='develop c#', salary=1000, work_experience='1 years')


passport1 = Passport.objects.create(employee=emp, inn=55365623156487, id_card=1665459685967485)
passport2 = Passport.objects.create(employee=emp1, inn=41585623156487, id_card=1666459685967485)
passport3 = Passport.objects.create(employee=emp2, inn=52955623156487, id_card=3216459685967485)
passport4 = Passport.objects.create(employee=emp3, inn=63595623156487, id_card=9876459685967485)

last_passport = Passport.objects.last()
last_passport.delete()

last_employee = last_passport.employee
last_employee.delete()

# project1 = WorkProjects.objects.create()
# project1.employees.set([emp, emp2, emp3, emp3])
# project1.save()

emp3.delete()

emp5 = Employee.objects.create(position='develop Ui/yi', salary=10000, work_experience='0.5 years')


client1 = Client.objects.create(adress='Chui', phone_number='996709441244')
client2 = Client.objects.create(adress='Vostok 5', phone_number='99622222222')
client3 = Client.objects.create(adress='Mossovet', phone_number='99674444444')
client4 = Client.objects.create(adress='DJAL', phone_number='996703446244')


vip_client1 = VIPClient.objects.create(vip_status_start='2020-05-01', donation_amount='5000')

client4.delete()


employees = Employee.objects.all()
for empp in employees:
    print(empp.position, empp.salary, empp.work_experience)

for empo in employees:
    passports = empo.passport
