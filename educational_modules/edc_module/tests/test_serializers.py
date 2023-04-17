import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from django.test import TestCase
from edc_module.models import EdcModule
from edc_module.serializers import EdcModuleSerializer


class EdcModuleSerializerTestCase(TestCase):
    def setUp(self):
        self.module_data = {
            'name': 'Test module',
            'description': 'This is a test module',
            'order_number': 1
        }
        self.module = EdcModule.objects.create(**self.module_data)
        self.serializer = EdcModuleSerializer(instance=self.module)

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.module_data['name'])

    def test_description_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['description'], self.module_data['description'])

    def test_order_number_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['order_number'], self.module.id)
