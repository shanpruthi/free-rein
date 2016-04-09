from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about', views.bout, name='about'),
    url(r'products', views.shit, name='products'),

]
