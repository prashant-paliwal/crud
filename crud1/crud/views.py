from django.shortcuts import render,redirect
from .models import employees
from django.http import HttpResponse
from .forms import EmployeeRegistrationModelForm
from django.db.models import Avg,Sum,Min,Max,Count
# Create your views here.


def employeeRegistration(request):
	if request.method=="POST":
		print(request.POST.get('registration_id'))
		registration_id = request.POST.get('registration_id',None)
		first_name = request.POST.get('first_name',None)
		last_name = request.POST.get('last_name',None)
		email = request.POST.get('email',None)
		role = request.POST.get('role',None)
		print(registration_id)
		form = employees(registration_id=registration_id,first_name=first_name,last_name=last_name,email=email,role=role)
		form.save()
		return HttpResponse('<h1>Employee has been registered ! <a href="/employees"> Back Home </a></h1>')
	else:
		pass
	return render(request,'crud/RegisterEmployeeForm.html')


def home(request):
	# emp_obj = employees.objects.all()
	emp_obj = employees.Teri.get_stu_roll_range(3,7)
	print("###########",emp_obj.explain())
	length = len(emp_obj)
	return render(request,'crud/home.html',{'empls':emp_obj,'length':length})

def specific(request,id=None):
	emp_obj = employees.objects.get(id=id)
	return render(request,'crud/specific.html',{'employee':emp_obj})

def delete(request,id=None):
	emp_obj = employees.objects.get(id=id)
	emp_obj.delete()
	return redirect('/employees')
	# return HttpResponse('<h1>Employee has been deleted! <a href="/employees"> Back Home </a></h1>')

def edit(request, id=None):
	emp_obj = employees.objects.get(id=id)

	if request.method=="POST":
		if request.POST.get('registration_id'):
			emp_obj.registration_id = request.POST.get('registration_id')

		if request.POST.get('first_name'):
			emp_obj.first_name = request.POST.get('first_name')

		if request.POST.get('last_name'):
			emp_obj.last_name = request.POST.get('last_name')

		if request.POST.get('email'):
			emp_obj.email = request.POST.get('email')

		if request.POST.get('role'):
			emp_obj.role = request.POST.get('role')

		emp_obj.save()
		return HttpResponse('<h1> Employee Details has been updated ! <a href="/employees"> Back Home</a> </h1>')

	else:
		pass
		
	return render(request,'crud/updateEmployee.html',{'empls':emp_obj})


def learning(request):
	# emp_obj = employees.objects.filter(id__in=[4,5,6])
	# emp_obj = employees.objects.filter(registration_id__in=[7,8,898])
	emp_obj = employees.objects.all()

	Average = emp_obj.aggregate(Avg('salary'))
	Total = emp_obj.aggregate(Sum('salary'))
	Minimum = emp_obj.aggregate(Min('salary'))
	Maximum = emp_obj.aggregate(Max('salary'))
	cnt = emp_obj.aggregate(Count('salary'))
	length = len(emp_obj)
	return render(request,'crud/home.html',{'empls':emp_obj,'length':length,'Average':Average,'Sum':Total,'Minimum':Minimum,'Maximum':Maximum,'Count':cnt})

