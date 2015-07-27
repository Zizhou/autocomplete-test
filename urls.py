from django.conf.urls import patterns, url

from complete import views

urlpatterns = patterns('',
    url(r'^$', views.main_page, name = 'main'),
    url(r'^/api/result$', views.api_result, name = 'api_result'),

)
