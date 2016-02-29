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

# imports for login & registration
from django.conf.urls import patterns
from newsweb.views import *


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^(?P<p_id>[0-9]+)/showpost',views.showpost),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^(?P<cat_id>[0-9]+)/cat', views.cat),
    url(r'^$', 'django.contrib.auth.views.login'),#defaultpage>localhost:8000
    url(r'^logout/$', logout_page),#click logout link
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
        # If user is not login it will redirect to login page
    url(r'^register/$', register),#click register button @ default page
    url(r'^register/success/$', register_success),#click register button @ RegPage
    url(r'^home/$', home),#click login button @ default page

    url(r'^(?P<tag_id>[0-9]+)/tag/$',views.tag_posts),
    url(r'^showpost/',views.showpost),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')), #Added Uploader url 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    url(r'^main/',views.main),

]
    
#urlpatterns += static(settings.MEDIA_URL, document_root=setting.MEDIA_ROOT

    


