from django.http import JsonResponse

from django_my_app_demo_rest.models.customer_models import Customer
from django_my_app_demo_rest.serializers.model_serializers import CustomerSerializer
from django_my_app_demo_rest.serializers.custom_serializers import CustomCustomerSerializer


def find_all_customer(request):
    if request.method == 'GET':
        qs = Customer.objects.all()
        print(qs.query)
        serializer = CustomerSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)


def find_customer_by_name(request, name):
    if request.method == 'GET':
        qs = Customer.objects.get(cust_kor_nm=name)
        # print(qs.query)
        serializer = CustomCustomerSerializer(qs)
        return JsonResponse(serializer.data)
