#from  django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url('', views.home, name='home'),
    url('about/', views.about, name='about'),
    url('blog/', include('blog.urls')),
    url('admin/', admin.site.urls),
]
#if settings.DEBUG:
#   import debug_toolbar
#   urlpatterns = [
#       url('__debug__/', include(debug_toolbar.urls)),
#   ] + urlpatterns
