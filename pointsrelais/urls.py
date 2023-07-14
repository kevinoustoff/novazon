"""
URL configuration for pointsrelais project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from relais.views import PointRelaisView
from relais.views import AllRelaisView
from relais.views import MapView


urlpatterns = [
   path('admin/', admin.site.urls),
   path('point_relais/', PointRelaisView.as_view(), name='point_relais'),
   path('all_relais/', AllRelaisView.as_view(), name='all_relais'),
   path('map/', MapView.as_view(), name='map'),  
   
]

