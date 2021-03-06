from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'gallery'

urlpatterns=[

  re_path(r'', views.home, name='home'),

  re_path(r'^search/', views.search_results, name='search'),
  re_path(r'^location/(?P<location>\w+)', views.home, name='location'),
  
  
] 
# + static(
#   settings.MEDIA_URL, 
#   document_root = settings.MEDIA_ROOT
# )
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)