from django.test import TestCase
from groups.models import Group

class GroupTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        group_data = {"name": "cão", "scientific_name": "canis familiaris"}
        Group.objects.create(**group_data)
    def test_groups_data(self):
        """Validate groups data"""
        group = Group.objects.all()[0]
        self.assertEqual('cão',group.name)
        self.assertEqual("canis familiaris",group.scientific_name)

    

        
