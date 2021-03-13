from django.shortcuts import render
from rest_framework import generics
from reservation.serializers import (
    MeetingDetailSerializer,
    MeetingListSerializer,
    MeetingSerializer,
)
from reservation.models import Meeting

from rest_framework.response import Response
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


@api_view(["GET"])
def read(request):

    meetings = Meeting.objects.all()
    serializer = MeetingSerializer(meetings, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def readbyid(request, pk):

    meeting = Meeting.objects.get(id=pk)
    serializer = MeetingSerializer(meeting, many=False)

    return Response(serializer.data)


@api_view(["POST"])
def create(request):

    serializer = MeetingSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def update(request, pk):
    meet = Meeting.objects.get(id=pk)
    serializer = MeetingSerializer(instance=meet, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def delete(request, pk):
    meet = Meeting.objects.get(id=pk)
    meet.delete()
    return Response({"message": "Deleted"})
