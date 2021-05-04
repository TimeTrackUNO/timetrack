
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from api import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('', views.movie_list),
    url(r'^api/movies/$', views.movie_list),
    url(r'^api/movies/(?P<pk>[0-9]+)$', views.getMovie),
    url(r'^api/events/$', views.timetracker_list),
    url(r'^api/time/$', views.time_list),
    url(r'^api/users/$', views. user_list),
    url(r'^api/event/$', views.event_list),
    url(r'^api/date/$', views.date_list),


]



