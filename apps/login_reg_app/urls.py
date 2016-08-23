from django.conf.urls import url
from views import index, login, register, success, logout, delete
urlpatterns = [
    url(r'^$', index, name='log_index'),
    url(r'login$', login, name='log_login'),
    url(r'register$', register, name='log_register'),
    url(r'success$', success, name='log_success'),
    url(r'logout$', logout, name='log_logout'),
    url(r'delete/(?P<user_id>\d+)$', delete, name='log_delete')
]
