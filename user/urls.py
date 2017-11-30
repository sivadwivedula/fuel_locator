from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', views.gov_notice.as_view()),    
    url(r'^(?P<pk>[0-9]+)/$', views.gov_notice_details.as_view()),    
    url(r'^fuel/$', views.fuel_list.as_view()),    
    url(r'^abc/$', views.PostExample.as_view(), name='test-start'),
    url(r'^accounts/update/(?P<pk>[\-\w]+)/$', views.update_user_details, name='account_update'),
    url(r'^otp_auth/$',views.get_otp,name='otp'),
    #url(r'^otp_regen/$',views.otp_gen,name='otp_regen'),

]
