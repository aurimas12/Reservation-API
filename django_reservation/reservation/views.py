from django.shortcuts import render
from rest_framework import generics
from reservation.serializers import MeetingDetailSerializer

# Create your views here.
class MeetingCreateView(generics.CreateAPIView):
    serializer_class = MeetingDetailSerializer
