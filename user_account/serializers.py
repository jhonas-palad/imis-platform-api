from collections import OrderedDict
from rest_framework import serializers
from rest_framework.exceptions import APIException
from django.core.exceptions import ValidationError as DjangoValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from phonenumber_field.serializerfields import PhoneNumberField, PhoneNumber

from app_platform.models import City
import logging
imis_logger = logging.getLogger("imis.stdout")
User = get_user_model()


example_data = {
    "first_name": "Jhonas Emmanuel",
    "last_name": "Palad",
    "email": "jhonas@gmail.com",
    "phone_number": "09394961849",
    "password": "raMpage@123",
    "re_password": "raMpage@123"
}
class CreateAccountSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone_number = PhoneNumberField(region="PH")
    password = serializers.CharField(required=True, write_only=True)
    re_password = serializers.CharField(required=True, write_only=True)
    def validate_password(self, password, *args, **kwargs):
        validate_password(password)
        return password
    def validate_phone_number(self, phone_number):
        if self.check_phone_number_is_unique(phone_number):
            raise serializers.ValidationError('The Phone number is already used.')
        return phone_number
    def validate_email(self, email):
        if self.check_email_is_unique(email):
            raise serializers.ValidationError('This email already used.')
        return email
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('re_password'):
            raise serializers.ValidationError({"re_password": "The two passwords do not match."})
        
        return attrs
    def is_valid(self, *, raise_exception=False):
        try:
            ret = super().is_valid(raise_exception=raise_exception)
        except serializers.ValidationError:
            self._errors = {
                "errors" : self._errors
            }
            raise serializers.ValidationError(self._errors)
        return ret
    def check_email_is_unique(self, email):
        return User.objects.filter(email=email).exists()
    def check_phone_number_is_unique(self, number):
        if isinstance(number, str):
            number = PhoneNumber.from_string(number)
        return User.objects.filter(phone_number=number).exists()
    
    def create(self, validated_data, cls = User, request = None):
        
        """
        This method should be run after is_valid
        """
        if hasattr(validated_data, "__contains__") and 're_password' in validated_data:
            del validated_data['re_password']
        if request is None:
            request = self.context['request']
        try:
            new_user = cls(**validated_data)
            new_user.full_clean()
        except DjangoValidationError as validation_err:
            self._errors = {"errors" : serializers.get_error_detail(validation_err)}
            print(self._errors)
        except Exception:
            raise APIException()
        else:
            new_user.set_password(validated_data['password'])
            new_user.save()
class CreateClientSerializer(CreateAccountSerializer):
    ...
    
class CreateProSerializer(CreateAccountSerializer):
    service_area_radius = serializers.IntegerField()
    base_address = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    
class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        required=True, 
        write_only=True,
        validators =[]
    )
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email","phone_number", "gender"]