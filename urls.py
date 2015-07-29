from django.conf.urls import patterns, url

from complete import views

urlpatterns = patterns('',
    url(r'^$', views.main_page, name = 'main'),
    #ew
    url(r'^api/get_id/$', views.api_get_none, name = 'none'),
    url(r'^api/get_id/(?P<game_id>.*)/$', views.api_get_id, name = 'api_get_id'),
    url(r'^api/search/$', views.api_search, name = 'api_search'),
)
