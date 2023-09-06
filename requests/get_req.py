import requests

# Define the API endpoint URL with the device ID you want to retrieve
device_id = "/devices/id12"  # Replace with the actual device ID
url = f"http://localhost:8000/api/devices/get-device/?id={device_id}"
# Send a GET request to retrieve a specific device
response = requests.get(url)

# Check the response
if response.status_code == 200:
    device = response.json()
    print("Device Information:")
    print(device)
elif response.status_code == 404:
    print("Device not found.")
else:
    print("Failed to retrieve the device.")
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
