from django.conf.urls import url
from . import views

app_name='blog'
urlpatterns = [
    url('', views.index, name='index'),
    url('posts/<int:id>-<slug:slug>', views.show, name='show'),
    url('contact/', views.contact,  name='contact'),
]
