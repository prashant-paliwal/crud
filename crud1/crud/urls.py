from django.urls import path
from crud import views
urlpatterns = [
    path('', views.home),
    path('registration', views.employeeRegistration),
    path('<int:id>', views.specific),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('learning', views.learning),
]