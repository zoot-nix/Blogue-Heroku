from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header  =  "Blogue Admin"  #Login 
admin.site.site_title  =  "Admin Site"
admin.site.index_title  =  "Blogue"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogueApp.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

