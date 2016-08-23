from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='gold_index'),
  url(r'^process_money/(?P<building>[a-zA-Z]+)$', views.process, name='gold_process')

  ]
