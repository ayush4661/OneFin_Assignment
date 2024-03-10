from django.urls import path
from .views import user_registration

urlpatterns = [
    path('register/', user_registration)
]
