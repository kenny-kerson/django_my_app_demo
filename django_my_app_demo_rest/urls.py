from django.urls import path
from django_my_app_demo_rest.views import snippet_views

urlpatterns = [
    path('snippets/', snippet_views.snippet_list),
    path('snippets/<int:pk>/', snippet_views.snippet_detail),
]