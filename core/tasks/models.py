from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_api_url(self):
        return reverse("core:root:tasks-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title
