from django.urls import path
from appname import views


app_name = 'appname'


urlpatterns = [
    path('', views.index, name='index.html'),
]