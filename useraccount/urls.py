from django.urls import path
from .views import CustomUserLoginView, CustomUserRegistration

urlpatterns = [
    path('create-account/', CustomUserRegistration.as_view(), name='create-account'),
    path('access-account/', CustomUserLoginView.as_view(), name='access-account')
]
