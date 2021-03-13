from django.shortcuts import render
from rest_framework import generics
from reservation.serializers import MeetingDetailSerializer, MeetingListSerializer
from reservation.models import Meeting
from rest_framework.decorators import api_view

# Create your views here.
class MeetingCreateView(generics.CreateAPIView):
    serializer_class = MeetingDetailSerializer


class MeetingListView(generics.ListAPIView):
    serializer_class = MeetingListSerializer
    queryset = Meeting.objects.all()


class MeetingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MeetingDetailSerializer
    queryset = Meeting.objects.all()
