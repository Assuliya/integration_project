from django.conf.urls import url, include
# from django.contrib import admin

urlpatterns = [

    url(r'^log-reg/', include('apps.login_reg_app.urls')),
    url(r'^courses/', include('apps.courses_model.urls')),
    url(r'^time/', include('apps.base_time.urls')),
    url(r'^ninja-gold/', include('apps.ninja_gold.urls')),
    url(r'^random-word/', include('apps.random_word.urls')),
    url(r'^', include('apps.multiple_apps.urls'))
]
