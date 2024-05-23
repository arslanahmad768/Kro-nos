from rest_framework.routers import DefaultRouter

from . import views


app_name = 'time_tracker'

router = DefaultRouter()

router.register(r'time_codes', views.TimeCodeViewSet, basename='time_code')
router.register(r'', views.IndirectHoursViewSet)

urlpatterns = []

urlpatterns += router.urls
