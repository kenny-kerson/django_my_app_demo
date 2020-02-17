# from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django_my_app_demo_rest.serializers.model_serializers import GroupSerializer
from django_my_app_demo_rest.serializers.model_serializers import UserSerializer


# def index(request):
#     context = {
#         'days': [1,2,3],
#     }
#
#     return render(request, 'index.html', context)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    print(queryset.query)
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    print(queryset.query)
    serializer_class = GroupSerializer
