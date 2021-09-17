from django.urls import path
from . import views


urlpatterns = [
    path('',views.shorten),
    path('<short>',views.redirecter, name='redirecter'),
    path('delete/<short>',views.delete, name='delete'),
    path('edit/<item>', views.edit, name='edit')
]