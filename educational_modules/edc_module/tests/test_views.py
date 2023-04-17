import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from rest_framework import status
from rest_framework.test import APITestCase
from edc_module.models import EdcModule


class EdcModuleViewSetTest(APITestCase):

   def test_list_edc_modules(self):
       response = self.client.get('/api/v1/modules/')
       self.assertEqual(response.status_code, status.HTTP_200_OK)

   def test_create_edc_module(self):
       data = {'name': 'Test Module', 'description': 'This is a test module',
               'order_number': 1}
       response = self.client.post('/api/v1/modules/', data)
       self.assertEqual(response.status_code, status.HTTP_201_CREATED)
       self.assertEqual(EdcModule.objects.count(), 1)
       self.assertEqual(EdcModule.objects.get().name, 'Test Module')

   def test_retrieve_edc_module(self):
       edc_module = EdcModule.objects.create(
           name='Test Module',
           description='This is a test module',
           order_number=1
       )
       response = self.client.get(f'/api/v1/modules/{edc_module.id}/')
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       self.assertEqual(response.data['name'], edc_module.name)

   def test_update_edc_module(self):
       edc_module = EdcModule.objects.create(
           name='Test Module',
           description='This is a test module',
           order_number=1
       )
       data = {'name': 'Updated Test Module',
               'description': 'This is an updated test module',
               'order_number': 2}
       response = self.client.put(f'/api/v1/modules/{edc_module.id}/', data)
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       edc_module.refresh_from_db()
       self.assertEqual(edc_module.name, 'Updated Test Module')

   def test_delete_edc_module(self):
       edc_module = EdcModule.objects.create(
           name='Test Module',
           description='This is a test module',
           order_number=1)
       response = self.client.delete(f'/api/v1/modules/{edc_module.id}/')
       self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
       self.assertEqual(EdcModule.objects.count(), 0)
