from django.urls import path ,include


app_name = 'tasks'


urlpatterns = [
    path('api/', include('tasks.api.v1.urls', namespace='v1')),
]
