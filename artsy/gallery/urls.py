from django.conf.urls import url,re_path,admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'gallery'

urlpatterns=[
  url(r'^$', views.home, name='home'),
  url(r'^search/', views.search_results, name='search'),
  re_path(r'^admin/$', admin.site.urls),
    # re_path('', include('artsy.urls')),
  re_path(r'^home/$', views.home, name='home'),

] + static(
  settings.MEDIA_URL, 
  document_root = settings.MEDIA_ROOT
)
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)