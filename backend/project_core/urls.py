from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path

from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



urlpatterns = [
    path('', include('platform_app.urls')),
]

## Swagger 설정 정보 (drf-yasg)
schema_view = get_schema_view(
   openapi.Info(
      title="Simple Project3 API",
      default_version='v0.1',
      description="simple-project3-api-document",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="oasisc1208@icloud.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[AllowAny],
)


if settings.DEBUG:      ## settings가 True가 되어 있는 경우에만 Swagger용 URL 등록
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^doc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]

