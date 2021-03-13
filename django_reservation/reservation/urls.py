from django.contrib import admin
from django.urls import path, include
from reservation.views import *

app_name = "reservations"
urlpatterns = [
    path("meet/create/", MeetingCreateView.as_view()),
    path("meet/all/", MeetingListView.as_view()),
    path("meet/detail/<int:pk>/", MeetingDetailView.as_view()),
    # path("meet/test/", meeting_view),
    path("meet/read/", read, name="test1"),
    path("meet/read/<str:pk>", readbyid, name="testdetail"),
    path("meet/create/>", create, name="testcreate"),
    path("meet/update/<str:pk>/", update, name="testcreate"),
    path("meet/delete/<str:pk>/", delete, name="testdelete"),
]
