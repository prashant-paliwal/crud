from django.db import models

# Create your models here.

class CustomManager(models.Manager):
	def get_stu_roll_range(self,r1,r2):
		return super().get_queryset().filter(id__range=(r1,r2))
	# def get_queryset(self):
	# 	return super().get_queryset().order_by('first_name')





EMPLOYEE_ROLE = (
	('BACKEND_DEVELOPER','BACKEND_DEVELOPER'),
	('FRONTEND_DEVELOPER', 'FRONTEND_DEVELOPER'),
	('HR','HR'),
	('DESINER','DESINER'),
	('MOBILE_DEVELOPER','MOBILE_DEVELOPER'),
)

class employees(models.Model):
	registration_id = models.IntegerField(null=True, blank=True)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.CharField(max_length=25)
	role = models.CharField(choices=EMPLOYEE_ROLE, max_length=20, null=True)
	salary = models.IntegerField(null=True,blank=True)

	objects = models.Manager() #Default Manager
	Teri = CustomManager()  # Custom Maneger

	def __str__(self):
		return self.first_name

