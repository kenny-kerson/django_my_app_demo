from rest_framework import serializers
from django_my_app_demo_rest.models.snippet_models import LANGUAGE_CHOICES
from django_my_app_demo_rest.models.snippet_models import STYLE_CHOICES
from django_my_app_demo_rest.models.snippet_models import Snippet


# OurSerializer
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


# OurSerializer
class AccountSerializer(serializers.Serializer):
    account_no = serializers.CharField()
    account_status = serializers.CharField()
    cstno = serializers.CharField()
    cust_kor_nm = serializers.CharField()


# OurSerializer
class CustomCustomerSerializer(serializers.Serializer):
    cstno = serializers.CharField()
    cust_kor_nm = serializers.CharField()
