from django.urls import re_path
from .views import ServiceView
urlpatterns = [
    re_path(r"services", ServiceView.as_view())
]