from django.conf.urls import url
from .import views
app_name='aces'

urlpatterns = [
    #/aces/
    url(r'^$',views.index,name='index'),
    #/aces/1/
   # url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
    #/aces/<album_id>/favorite/

    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),



]
