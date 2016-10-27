from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^profile/$', views.about_me, name='about_me'),
    url(r'^contact/$', views.contact_me, name='contact_me'),
    url(r'^projects/$', views.my_portfolio, name='my_portfolio'),
    url(r'^post/(?P<pk>\d+)/$', views.project_detail, name='project_detail'),
]
