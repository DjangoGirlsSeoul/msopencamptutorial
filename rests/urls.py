from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.rest_list,name="rest_list")
]