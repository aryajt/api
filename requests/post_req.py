import requests

# Define the API endpoint URL
url = "http://localhost:8000/api/devices/create/"

# Define the JSON payload for creating a device
payload = {
    "id": "11",
    "deviceModel": "/devicemodels/id1",
    "name": "Sensor",
    "note": "Testing a sensor.",
    "serial": "A020000102"
}

# Send a POST request to create a device
response = requests.post(url, json=payload)

# Check the response
if response.status_code == 201:
    print("Device created successfully.")
    print("Response JSON:", response.json())
else:
    print("Failed to create device.")
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
