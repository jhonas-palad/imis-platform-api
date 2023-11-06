
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from .serializers import UserSerializer
class CreateAccount(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request:Request, *args, **kwargs):
        """
        data = {
            user_type: "client" or "pro",
            firstname: string,
            lastname: string,
            phone_number: string,
            email: string
            password: string,
            confirm_password: string
        }
        """
        user_type = self.get_user_type() or "client"
        
    def get_user_type(self) -> str | None:
        return self.request.data.get("user_type", None)