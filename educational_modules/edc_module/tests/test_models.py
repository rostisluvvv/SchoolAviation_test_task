import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
from django.test import TestCase
from edc_module.models import EdcModule


class EdcModuleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        EdcModule.objects.create(name='Test Module',
                                 description='This is a test module')

    def test_name_max_length(self):
        module = EdcModule.objects.get(id=1)
        max_length = module._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_description_blank(self):
        module = EdcModule.objects.get(id=1)
        blank = module._meta.get_field('description').blank
        self.assertTrue(blank)

    def test_description_null(self):
        module = EdcModule.objects.get(id=1)
        null = module._meta.get_field('description').null
        self.assertTrue(null)

    def test_str_method(self):
        module = EdcModule.objects.get(id=1)
        expected_string = f'{module.name}'
        self.assertEqual(str(module), expected_string)




