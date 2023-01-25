"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import py_compile
from django.contrib import admin
from django.urls import path, include
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
"""
from firstproject import views
 
urlpatterns = [
    path('admin-panel', admin.site.urls),
    
    path('',views.homepage),
    path('prod',views.products),
    path('thn',views.thanks),
    path('con',views.contact),
    path('prod_des',views.prod_des),
    path('Ann_rtn', views.annual_return),
    path('',include('login.urls')),
]

