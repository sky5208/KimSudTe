from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about),
    path('form',views.form),
    path('edit/<customer_code>',views.edit),
    path('delete/<customer_code>',views.delete),
    path('customer',views.customer),
    
]