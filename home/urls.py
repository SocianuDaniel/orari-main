
from django.urls import path, include
from home import views
from django.views.generic import TemplateView

app_name = 'home'
urlpatterns = [
    path('',views.ListTurni.as_view(),name="home"),
    path('<str:data>/',views.ListTurni.as_view(),name="list-by-date"),

]
