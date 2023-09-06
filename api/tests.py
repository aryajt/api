from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Device

class DeviceAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.device_data = {
            "id": "test_id",
            "deviceModel": "Test Model",
            "name": "Test Device",
            "note": "Test Note",
            "serial": "Test Serial"
        }
        self.url_create_device = reverse("create_device")
        self.url_get_device = reverse("get_device")

    def test_create_device(self):
        response = self.client.post(self.url_create_device, self.device_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Device.objects.count(), 1)
        self.assertEqual(Device.objects.get().name, "Test Device")

    def test_create_device_invalid_data(self):
        # Test creating a device with invalid data
        invalid_data = {"deviceModel": "Invalid Model"}  # Missing required fields
        response = self.client.post(self.url_create_device, invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_device(self):
        device = Device.objects.create(**self.device_data)
        response = self.client.get(f"{self.url_get_device}?id={device.id}", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Device")

    def test_get_device_missing_id(self):
        response = self.client.get(self.url_get_device, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_device_not_found(self):
        response = self.client.get(f"{self.url_get_device}?id=nonexistent_id", format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


