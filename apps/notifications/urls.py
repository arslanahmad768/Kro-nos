from rest_framework.routers import DefaultRouter

from . import views


app_name = 'notifications'

router = DefaultRouter()

router.register(r'', views.ActionViewSet)

urlpatterns = []

urlpatterns += router.urls
