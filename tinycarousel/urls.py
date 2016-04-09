from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'bout', views.bout, name='bout'),
    url(r'shit', views.shit, name='shit'),

]
