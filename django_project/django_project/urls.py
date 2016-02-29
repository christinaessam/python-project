"""django_project URL Configuration

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

from django.conf.urls import url,include
from django.contrib import admin
from newsweb import views 
from django_project import settings
#from django.conf.urls.static import static
#import settings
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^(?P<p_id>[0-9]+)/showpost',views.showpost),
    url(r'^addpost/',views.createpost),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^(?P<cat_id>[0-9]+)/cat', views.cat),
   # url(r'^',views.showpost),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')), #Added Uploader url 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
]
    
#urlpatterns += static(settings.MEDIA_URL, document_root=setting.MEDIA_ROOT






