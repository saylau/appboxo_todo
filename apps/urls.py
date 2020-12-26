from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .users.views import UserViewSet, UserCreateViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)

internal_schema_view = get_schema_view(
    openapi.Info(
        title="Todo API", default_version="v1", description="Todo",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # urlconf="apps.urls"
)

urlpatterns = [
    path("api/", include("apps.todos.urls")),
    path("api/", include("apps.categories.urls")),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(
      "api/docs/",
      internal_schema_view.with_ui("swagger", cache_timeout=0),
      name="schema-swagger-ui",
    ),
    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
