import os

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from django4e import settings

# Up two folders to serve "site" content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    re_path(r'^site/(?P<path>.*)$', serve,
            {'document_root': os.path.join(BASE_DIR, "django4e/", 'site'),
             'show_indexes': True},
            name='site_path'
            ),
]