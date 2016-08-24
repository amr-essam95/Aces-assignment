from django.conf.urls import url
from . import views


urlpatterns =[
    # /aces/
    url(r'^$',views.index,name='index'),

    #/aces/712/
    url(r'^register/$',views.UserFormView.as_view(),name='register')
]