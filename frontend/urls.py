from django.urls import path
from apps.student import views


urlpatterns = [
    path('', views.index, name='index'),
]

