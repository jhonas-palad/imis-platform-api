from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
import logging
imis_logger = logging.getLogger("imis.stdout")
User = get_user_model()



class CreateClientSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    re_password = serializers.CharField(required=True, write_only=True)
    def validate_password(self, password, *args, **kwargs):
        validate_password(password)
        return password
    def validate(self, attrs):
        if attrs.password != attrs.re_password:
            raise serializers.ValidationError({"re_password": "Passwords do not match."})
        return attrs
class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        required=True, 
        write_only=True,
        validators =[]
    )
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email","phone_number", "gender"]