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
    
    url(r'^add-ticket/', views.add, name='add'),
    url(r'^my-tickets/', views.tickets, name='tickets'),
    
    url(r'^view-ticket/(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^edit/(?P<id>[0-9]+)/$', views.edit, name='edit'),
    
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^alter-status', views.alter_status, name='status'),
]
