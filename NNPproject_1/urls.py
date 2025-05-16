"""
URL configuration for NNPproject_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

admin.site.site_header = "ICAR-IIRR NNP Database Admin"
admin.site.site_title = "ICAR-IIRR NNP Database Admin Portal"
admin.site.index_title = "Welcome to ICAR-IIRR NNP Database"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('Search', include('Home.urls')),
    path('Team', include('Home.urls'))
]
