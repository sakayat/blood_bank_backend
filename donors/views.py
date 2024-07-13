from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status, permissions
from .serializers import DonorProfileSerializer, BloodRequestSerializer, DonationHistorySerializer
from .models import DonorProfile, BloodRequest, DonationHistory


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
            return Response(
                {"error": "user details already exits"}, status.HTTP_400_BAD_REQUEST
            )
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
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        donor = self.get_object(pk)
        donor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BloodRequestAPI(APIView):
    serializer_class = BloodRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        blood_requests = BloodRequest.objects.exclude(donor=request.user)
        serializer = BloodRequestSerializer(blood_requests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BloodRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(donor=request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class AcceptBloodRequestAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def put(self, request, id, format=None):
        try:
            blood_request = BloodRequest.objects.get(pk=id)
        except BloodRequest.DoesNotExist:
            return Response({'error': 'Blood request not found'})
        
        
        donor = blood_request.donor
        recipient = request.user

        donation_history = DonationHistory.objects.create(
            donor=donor,
            recipient=recipient,
            status='accepted'
        )

        blood_request.status = 'accepted'
        blood_request.save()

        serializer = DonationHistorySerializer(donation_history)
        return Response(serializer.data, status.HTTP_200_OK)
    
class CancelBloodRequest(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, id, format=None):
        try:
            blood_request = BloodRequest.objects.get(pk=id)
        except BloodRequest.DoesNotExist:
            return Response({'error': 'Blood request not found'})
        
        if blood_request.status == "accepted":
            blood_request.status = "canceled"
            blood_request.save()
            
            donations = DonationHistory.objects.filter(donor=blood_request.donor,recipient=request.user).first()
            if donations:
                donations.status = "canceled"
                donations.save()
            
            serializer = BloodRequestSerializer(blood_request)
            return Response(serializer.data, status.HTTP_200_OK)
        elif blood_request.status == "canceled":
            return Response({"error": "Request already canceled"})
        else:
            return Response({"error": "Cannot cancel this request"})
            
    
class DonationHistoryAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        donations = DonationHistory.objects.filter(recipient=request.user)
        serializer = DonationHistorySerializer(donations, many=True)
        return Response(serializer.data)
    

class OngoingBloodRequestAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        requests = BloodRequest.objects.filter(status="pending")
        serializer = BloodRequestSerializer(requests, many=True)
        return Response(serializer.data)