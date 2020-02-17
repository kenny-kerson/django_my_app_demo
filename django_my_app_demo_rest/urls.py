from django.urls import path
from django_my_app_demo_rest.views import snippet_views
from django_my_app_demo_rest.views import customer_views
from django_my_app_demo_rest.views import account_views

urlpatterns = [
    path('snippets/', snippet_views.snippet_list),
    path('snippets/<int:pk>/', snippet_views.snippet_detail),

    path('customer/', customer_views.find_all_customer),
    path('customer/<str:name>/', customer_views.find_customer_by_name),

    path('account/<str:account_no>/', account_views.find_account_and_customer_info_by_account_no)
]