from django.urls import path
from rest_framework import routers
from .views import TaskViewSet

app_name = 'v1'
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks_rout')
urlpatterns = router.urls
