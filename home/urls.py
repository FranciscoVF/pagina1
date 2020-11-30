from django.urls import path

from home import views

app_name = "paginas"

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
]
