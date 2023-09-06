import requests

# Define the API endpoint URL
url = "http://localhost:8000/api/devices/all"

# Send a GET request to retrieve all devices
response = requests.get(url)

# Check the response
if response.status_code == 200:
    devices = response.json()
    if devices:
        print("All Devices:")
        for device in devices:
            print(device)
    else:
        print("No devices found.")
else:
    print("Failed to retrieve devices.")
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
