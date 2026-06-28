from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/',views.Emp_details, name='Emp_details'),
]