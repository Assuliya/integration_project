from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='random_index'),
  url(r'^generate$', views.get_num, name='random_generate')

  ]
