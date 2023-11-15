
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, CreateClientSerializer, CreateProSerializer
from .models import User, Professional
import logging
logger = logging.getLogger('imis.stdout')
p_d = logger.debug

#TODO
# Can only access by no auth token
class CreateClientAccount(GenericAPIView):
    serializer_class = CreateClientSerializer
    response_messages = {
        status.HTTP_201_CREATED : "Account created successully",
        "error": "Failed to create the account"
    }
    def get(self, request):
        return Response(data={"success": f"method {request.method}"})
    def post(self, request:Request, *args, **kwargs):
        p_d("Creating account")
        serializer: CreateClientSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        if(serializer.errors):
            return Response(data=serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        return Response(data={
            "success": self.response_messages[status.HTTP_201_CREATED]
        }, status=status.HTTP_201_CREATED)
    
class CreateProAccount(GenericAPIView):
    serializer_class = CreateProSerializer
    def post(self, request, *args, **kwargs):
        serializer: CreateClientSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        p_d(f"Account created with id {user.id}")
        return Response(data={
            "success": self.response_messages[status.HTTP_201_CREATED]
        }, status=status.HTTP_201_CREATED)
