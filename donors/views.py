from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .serializers import DonorProfileSerializer, BloodEventRequestSerializer
from .models import DonorProfile, BloodEventRequest

# Create your views here.
class DonorProfileAPI(APIView):
    serializer_class = DonorProfileSerializer
    
    def get(self, request, format=None):
        donor = DonorProfile.objects.get(donor=request.user)
        serializer = DonorProfileSerializer(donor)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        donor = DonorProfile.objects.get(donor=request.user)
        if donor:
            return Response({"error": "user details already exits"} , status.HTTP_400_BAD_REQUEST)
        serializer = DonorProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(donor=request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    

class UpdateDonorProfileAPI(APIView):
    serializer_class = DonorProfileSerializer
    
    def get_object(self, pk):
        return DonorProfile.objects.get(pk=pk)
    
    def get(self, request, pk, format=None):
        donor = self.get_object(pk)
        serializer = DonorProfileSerializer(donor)
        return Response(serializer.data)
    
    
    def put(self, request, pk, format=None):
        donor = self.get_object(pk)
        serializer = DonorProfileSerializer(donor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        donor = self.get_object(pk)
        donor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BloodEventRequestAPI(APIView):
    serializer_class = BloodEventRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        blood_requests = BloodEventRequest.objects.all()
        serializer = BloodEventRequestSerializer(blood_requests, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = BloodEventRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(donor=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

