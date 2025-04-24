import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from tasks.models import Task


@pytest.fixture
def user_fixture():
    return User.objects.create_user(username="testuser", password="testpass")


@pytest.fixture
def task_fixture(user_fixture):
    return Task.objects.create(
        user=user_fixture,
        title="Test Task",
        description="This is a test task.",
        is_completed=False
    )


@pytest.fixture
def client():
    return APIClient()

@pytest.mark.django_db(True)
class TestTask:
    def test_unauthorize_user(self, client):
        url = reverse('tasks:v1:tasks_rout-list')
        response = client.get(url)
        assert response.status_code == 403

    def test_unauthorize_user_send_data(self, client, task_fixture):
        url = reverse("tasks:v1:tasks_rout-list")
        data = {
            "title": task_fixture.title,
            "description": task_fixture.description,
            "is_completed": task_fixture.is_completed,
            "user": task_fixture.user.id
        }
        response = client.post(url, data, format='json')
        assert response.status_code in [401, 403]

    def test_authorized_user_send_data(self, client, user_fixture, task_fixture):
        client.force_authenticate(user=user_fixture) 
        url = reverse("tasks:v1:tasks_rout-list")
        data = {
            "title": task_fixture.title,
            "description": task_fixture.description,
            "is_completed": task_fixture.is_completed,
            "user": user_fixture.id
        }
        response = client.post(url, data, format='json')
        assert response.status_code == 201
