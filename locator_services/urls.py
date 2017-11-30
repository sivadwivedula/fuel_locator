from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
import user
from django.views.generic.base import RedirectView
urlpatterns = [
    url(r'^accounts/', include('registration.backends.default.urls')),        
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls',namespace='settings')),
    url(r'^$', RedirectView.as_view(url='/user/')),
    url(r'^contact/', views.contact),
]
