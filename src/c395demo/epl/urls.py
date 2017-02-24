from django.conf.urls import url

from . import views

from epl.views import (login_view, logout_view)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hardware/', views.hardware, name='hardware'),
    url(r'^software/', views.software, name='software'),
    url(r'^manage-tickets/', views.manage, name='manage'),
    url(r'^general/', views.general, name='general'),
    url(r'^password-recovery/', views.password, name='password'),
    url(r'^service-request/', views.service, name='service'),
    
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
]
