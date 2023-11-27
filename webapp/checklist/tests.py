from django.test import TestCase
from .models import Resource

# Create your tests here.

class ResourceModelTests(TestCase):
    def test_resource_creation(self):
        Resource(
            found=False, 
            location='https://mapgenie.io/elden-ring/maps/the-lands-between?locationIds=164509',
            name='Blue Dancer Charm', 
            category='BOSS', 
            region='LIMGRAVE', 
            info='Additional Info').save()
        bd_data = Resource.objects.get(name='Blue Dancer Charm')
        self.assertEqual(bd_data.found, False)
        self.assertEqual(bd_data.location, 'https://mapgenie.io/elden-ring/maps/the-lands-between?locationIds=164509')
        self.assertEqual(bd_data.category, 'BOSS')
        self.assertEqual(bd_data.region, 'LIMGRAVE')
        self.assertEqual(bd_data.info, 'Additional Info')
