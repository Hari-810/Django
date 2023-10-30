from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task

class TaskAPITest(APITestCase):
    def setUp(self):
        self.task_data = {'title': 'Test Task', 'description': 'This is a test task.'}
        self.task = Task.objects.create(**self.task_data)
        self.url = reverse('task-list-create')
        self.detail_url = reverse('task-detail', kwargs={'pk': self.task.id})

    def test_create_task(self):
        response = self.client.post(self.url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_task_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_task_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        updated_data = {'title': 'Updated Task', 'description': 'This is an updated task.'}
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
