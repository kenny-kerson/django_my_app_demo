"""django_my_app_demo URL Configuration

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
# from django.conf.urls import url
# from django.contrib import admin
# from django.urls import path
#
# from django_my_app_demo.views import index
#
# urlpatterns = [
#     url(r'admin/', admin.site.urls),
#     url(r'^$', index),
# ]

from django.urls import include, path
from rest_framework import routers
from django_my_app_demo_rest.views import auth_views

router = routers.DefaultRouter()
router.register(r'users', auth_views.UserViewSet)
router.register(r'groups', auth_views.GroupViewSet)

api_urls = [
    path('', include('django_my_app_demo_rest.urls')),
]

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(api_urls)),
]