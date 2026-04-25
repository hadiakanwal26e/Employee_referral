from django.urls import path
from . import views

urlpatterns = [
    path('', views.showAll, name='showAll'),
    path('insert/', views.insertEmployee, name='insertEmployee'),
    path('delete/', views.deleteEmployee, name='deleteEmployee'),
    path('update/', views.updateEmployee, name='updateEmployee'),
]