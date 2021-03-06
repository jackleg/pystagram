"""pystagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from profiles.urls import urlpatterns as profile_urls

urlpatterns = [
    url(r'^accounts/login/', 'django.contrib.auth.views.login',
        name='login', kwargs={'template_name': 'login.html'}),
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^photo/upload/$', 'photo.views.new_photo', name='new_photo'),
    url(r'^admin/', admin.site.urls),
    url(r'^photo/(?P<photo_id>\d+)$', 'photo.views.single_photo', name='view_single_photo'),
    url(r'^user/', include(profile_urls, namespace='profiles'),),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
