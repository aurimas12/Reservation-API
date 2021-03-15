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

from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class MeetingCreateView(generics.CreateAPIView):

    serializer_class = MeetingDetailSerializer


class MeetingListView(generics.ListAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MeetingListSerializer
    queryset = Meeting.objects.all()


class MeetingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MeetingDetailSerializer
    queryset = Meeting.objects.all()


@api_view(["GET"])
def read(request):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = (IsAuthenticated,)
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
    meetings = Meeting.objects.all()
    data = request.data
    ids = []
    for i in meetings:
        if i.date == data['date']:
            ids.append(str(i.id))

    for i in meetings:
        for idx in range(len(ids)):
            if idx == i.id:
                if i.start_time == request.data['start_time']:
                    print(False)

                # print(i.start_time, i.end_time)

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
