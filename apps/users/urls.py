from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CustomerViewSet, AdminProfileViewSet
from .views import UserRegistrationView, UserLoginView, UserLibraryView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'admins', AdminProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register-form/', UserRegistrationView.as_view(), name='user_register_form'),
    path('login/', UserLoginView.as_view(), name='user_login_form'),
    path('library/', UserLibraryView.as_view(), name='user_library'),
]
