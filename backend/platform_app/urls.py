from django.urls import include, path, re_path
from rest_framework import routers
from platform_app import views #views.py import


app_name = "platform_app"

router = routers.DefaultRouter()
router.register(r"products", views.BasicViewSet, basename="basic API")


# urlpatterns = router.urls
urlpatterns = [
    path('shop/', include(router.urls)),
]