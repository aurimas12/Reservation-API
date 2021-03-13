from django.contrib import admin
from django.urls import path, include
from reservation.views import *

app_name = "reservations"
urlpatterns = [
    path("meet/create/", MeetingCreateView.as_view()),
    path("meet/all/", MeetingListView.as_view()),
    path("meet/detail/<int:pk>/", MeetingDetailView.as_view()),
]
