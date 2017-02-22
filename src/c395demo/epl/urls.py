from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hardware/', views.hardware, name='hardware'),
    url(r'^software/', views.software, name='software'),
    url(r'^login/', views.login, name='login'),
    url(r'^manage-tickets/', views.manage, name='manage'),
    url(r'^general/', views.general, name='general'),
]
