
# local Django
from .models import *

# Django library

# Third-party
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

class MeetingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ("id", "title", "start_time", "date")


class MeetingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = "__all__"


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = "__all__"


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password',
                  'first_name', 'last_name')
