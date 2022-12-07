from django.test import TestCase
from traits.models import Trait

class TraitTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        trait_data = {"name": "peludo"}
        Trait.objects.create(**trait_data)

    def test_traits_data(self):
        """Validate traits data"""
        trait = Trait.objects.all()[0]
        self.assertEqual("peludo",trait.name)
        
