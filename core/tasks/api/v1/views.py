from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from tasks.models import Task
from .serializers import TasksSerializers
from .pagination import CustomPagination
from rest_framework import filters


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TasksSerializers
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
