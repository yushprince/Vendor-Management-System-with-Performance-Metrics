from django.test import TestCase
# import os
# import django
#
# # Set the DJANGO_SETTINGS_MODULE environment variable
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vendor_management_project.settings')
#
# # Initialize Django
# django.setup()

# Import necessary modules after Django is initialized

from django.urls import reverse
from .models import Vendor, PurchaseOrder

class APITestCase(TestCase):
    def test_vendor_api(self):
        # Create a vendor
        response = self.client.post(reverse('vendor-list-create'), {'name': 'Test Vendor', 'vendor_code': '123'})
        self.assertEqual(response.status_code, 201)

        # Retrieve the vendor
        vendor_id = response.data['id']
        response = self.client.get(reverse('vendor-detail', args=[vendor_id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Vendor')

        # Update the vendor
        response = self.client.put(reverse('vendor-detail', args=[vendor_id]), {'name': 'Updated Vendor'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Updated Vendor')

        # Delete the vendor
        response = self.client.delete(reverse('vendor-detail', args=[vendor_id]))
        self.assertEqual(response.status_code, 204)

