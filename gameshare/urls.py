from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="GameShare API",
        default_version='v1',
        description="API documentation for the Game Rental System",
        terms_of_service="https://example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
    path('games/', include('apps.games.urls')),
    path('transactions/', include('apps.transactions.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='user_login_form'), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)