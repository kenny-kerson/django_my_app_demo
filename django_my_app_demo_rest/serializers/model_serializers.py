from django.contrib.auth.models import User, Group
from rest_framework import serializers

from django_my_app_demo_rest.models.customer_models import Customer
from django_my_app_demo_rest.models.account_models import Account

# ModelSerializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

# ModelSerializer
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# ModelSerializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['cstno', 'cust_kor_nm']

