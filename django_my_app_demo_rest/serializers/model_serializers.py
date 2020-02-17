from django.contrib.auth.models import User, Group
from rest_framework import serializers

from django_my_app_demo_rest.models import Customer, LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


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
class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['cstno', 'cust_kor_nm']

