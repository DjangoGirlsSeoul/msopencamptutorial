from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.rest_list,name="rest_list"),
    url(r'^rest/(?P<pk>\d+)/$',views.rest_detail,name="rest_detail"),
    url(r'^rest/new/$', views.rest_new, name='rest_new'),
]
