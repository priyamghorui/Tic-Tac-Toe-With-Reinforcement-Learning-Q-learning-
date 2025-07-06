"""
URL configuration for ticTactoe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index,name="index"),
    path("move/", views.move,name="move"),
    path("agentMove/", views.agentMove,name="agentMove"),
    path("userMove/", views.userMove,name="userMove"),
    path("sessionClear/", views.sessionClear,name="sessionClear"),
    path("status/", views.status,name="status"),
    path("agentmovesecond/", views.agentmovesecond,name="agentmovesecond"),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
