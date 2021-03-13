from rest_framework import serializers
from reservation.models import Meeting


class MeetingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = "__all__"
