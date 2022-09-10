from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('sucess/',views.sucess,name = 'sucess'),
    path('<str:key>/',views.download_file,name = 'download'),
]