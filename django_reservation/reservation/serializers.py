from rest_framework import serializers
from reservation.models import Meeting


class MeetingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ("id", "title", "start_time", "date")


class MeetingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = "__all__"