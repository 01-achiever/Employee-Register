from django.urls import path, include
from . import views

urlpatterns = [
    path('employee/',views.employee_form,name='employee'),
    path('list/<int:id>',views.employee_list,name="employee_list"),
    path('employee_delete/<int:id>',views.employee_delete,name="Delete"),
    path('update/<int:id>',views.update,name="update"),

]


