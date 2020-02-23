import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView, RedirectView

admin_path=os.getenv("ADMIN_SITE_PATH")

urlpatterns = [
    path( (admin_path+ '/'), admin.site.urls),
    path('', TemplateView.as_view(template_name='index.view')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/', include('apiv1.urls')),
    re_path('', RedirectView.as_view(url='/')),
]
