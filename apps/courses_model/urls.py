from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='course_index'),
  url(r'^delete/(?P<user_id>\d+)$',views.delete, name='course_delete'),
  url(r'^destroy/(?P<user_id>\d+)$',views.destroy, name='course_destroy'),
  url(r'^register$',views.register, name='course_register'),
  url(r'^back$',views.back, name='course_back')

  ]
