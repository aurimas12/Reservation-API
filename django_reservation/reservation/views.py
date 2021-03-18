# local library
# local Django
from reservation.models import Meeting
from reservation.serializers import (
    MeetingDetailSerializer,
    MeetingListSerializer,
    MeetingSerializer,
    )
    
# Django
from django.shortcuts import render

# Third-party
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,status


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request, *args, **kwargs):
    return Response(data='Only for Logged in User', status=status.HTTP_200_OK)


class MeetingCreateView(generics.CreateAPIView):
    serializer_class = MeetingDetailSerializer

    def create(self, request, *args, **kwargs):
        data=request.POST
        if data['employees'].isdigit():
            return super(MeetingCreateView, self).create(request, *args, **kwargs)
        else:
            return Response('In employees field you must write number, not letter!')
        

class MeetingListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MeetingListSerializer
    queryset = Meeting.objects.all()


class MeetingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MeetingDetailSerializer
    queryset = Meeting.objects.all()


@api_view(["GET"])
def read(req):
    meetings = Meeting.objects.all()
    serializer = MeetingSerializer(meetings, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def readbyid(req, pk):
    meeting = Meeting.objects.get(id=pk)
    serializer = MeetingSerializer(meeting, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def update(req, pk):
    meet = Meeting.objects.get(id=pk)
    serializer = MeetingSerializer(instance=meet, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def delete(req, pk):
    meet = Meeting.objects.get(id=pk)
    meet.delete()
    return Response({"message": "Deleted"})
