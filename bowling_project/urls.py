from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
  openapi.Info(
      title="Bowling Scoresheet API",
      default_version="v1",
  ),
  public=True,
  permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("scoring_app.urls")),
    path("api/v1/", include("scoring_app.api.urls")),
    path("swagger-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
