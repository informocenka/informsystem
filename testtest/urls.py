from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.base_page, name = 'base_page'),
    url(r'^valuation/(?P<pk>\d+)/$', views.valuation_result, name='valuation_result'),
    url(r'^valuation/new/$', views.valuation_new, name = 'valuation_new'),

    ]