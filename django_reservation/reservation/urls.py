from django.contrib import admin
from django.urls import path, include
from reservation.views import *

app_name = "reservations"
urlpatterns = [path("meet/create/", MeetingCreateView.as_view())]
