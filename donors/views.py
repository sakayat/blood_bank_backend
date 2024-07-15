from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status, permissions
from .serializers import DonorSerializer, BloodRequestSerializer, DonationHistorySerializer
from .models import Donor, BloodRequest, DonationHistory


# Create your views here.
class DonorProfileAPI(APIView):
    serializer_class = DonorSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        donor = Donor.objects.filter(donor=request.user)
        if donor:
            donor = Donor.objects.get(donor=request.user)
            serializer = DonorSerializer(donor)
            return Response(serializer.data)
        return Response({"error": "No profile details available"})

    def post(self, request, format=None):
        donor = Donor.objects.filter(donor=request.user)
        if donor:
            return Response(
                {"error": "user details already exits"}, status.HTTP_400_BAD_REQUEST
            )
        serializer = DonorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(donor=request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UpdateDonorProfileAPI(APIView):
    serializer_class = DonorSerializer

    def get_object(self, pk):
        return Donor.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        donor = self.get_object(pk)
        serializer = DonorSerializer(donor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        donor = self.get_object(pk)
        serializer = DonorSerializer(donor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        donor = self.get_object(pk)
        donor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DonorListAPI(APIView):
    def get(self, request, format=None):
        donors = Donor.objects.filter(is_available=True)
        serializer = DonorSerializer(donors, many=True)
        return Response(serializer.data)

class BloodRequestAPI(APIView):
    serializer_class = BloodRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        blood_requests = BloodRequest.objects.filter(donor=request.user)
        serializer = BloodRequestSerializer(blood_requests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BloodRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(donor=request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    

class BloodRequestListAPI(APIView):
    def get(self, request):
        blood_group = request.query_params.get('blood_group')
        blood_requests = BloodRequest.objects.all()
        if blood_group:
            blood_requests = blood_requests.filter(blood_group=blood_group)
        serializer = BloodRequestSerializer(blood_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AcceptBloodRequestAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, id, format=None):
        try:
            blood_request = BloodRequest.objects.get(pk=id)
        except BloodRequest.DoesNotExist:
            return Response({'error': 'Blood request not found'})
        
       
        
        donor = blood_request.donor
        recipient = request.user
        
        if donor == recipient:
            return Response("you can not accept your own request")

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