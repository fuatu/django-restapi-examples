"""djrest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstapp/', include('firstapp.urls')),
    path('secondapp/', include('secondapp.urls')),
    path('thirdapp/', include('thirdapp.urls')),
    path('fourthapp/', include('fourthapp.urls')),
    path('fifthapp/', include('fifthapp.urls')),
    path('sixthapp/', include('sixthapp.urls')),
    path('seventhapp/', include('seventhapp.urls')),
    path('fileupload/', include('fileupload.urls')),
    path('', lambda request: redirect('api-docs/', permanent=False)),
    path('api-docs/', include_docs_urls(title='Rest API', description="All api details here")),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)