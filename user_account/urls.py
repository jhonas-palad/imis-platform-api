from django.urls import re_path
from .views import CreateAccount

urlpatterns = [
    re_path(r"$create", CreateAccount.as_view())
]