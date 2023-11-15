from django.urls import re_path
from .views import CreateClientAccount

urlpatterns = [
    re_path(r"create/client", CreateClientAccount.as_view())
]