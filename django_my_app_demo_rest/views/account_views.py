from django.db.models import Subquery
from django.http import JsonResponse

from django_my_app_demo_rest.models.account_models import Account
from django_my_app_demo_rest.models.customer_models import Customer
from django_my_app_demo_rest.serializers.custom_serializers import AccountSerializer


def find_account_and_customer_info_by_account_no(request, account_no):
    if request.method == 'GET':
        qs1 = Account.objects.get(account_no=account_no)
        print(qs1)
        qs2 = Customer.objects.get(cstno=qs1.user_id)
        print(qs2)
        qs = {
            'account_no': qs1.account_no,
            'account_status': qs1.account_status,
            'cstno': qs2.cstno,
            'cust_kor_nm': qs2.cust_kor_nm,
        }
        serializer = AccountSerializer(qs)
        return JsonResponse(serializer.data)
