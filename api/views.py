from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Devices_test  
from .serializers import DeviceSerializer

@api_view(['POST'])
def create_device(request):
    serializer = DeviceSerializer(data=request.data)
    if serializer.is_valid():
        device_data = serializer.validated_data
        device = Devices_test(**device_data)
        device.save_to_dynamodb()  
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_device(request):
    id = request.query_params.get('id')
    
    if not id:
        return Response({'detail': 'ID parameter is missing'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        device = Devices_test.get_device_by_id(id)  
        serializer = DeviceSerializer(device)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Devices_test.DoesNotExist:
        return Response({'detail': 'Device not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_devices(request):
    devices = Devices_test.get_all_devices()  
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
