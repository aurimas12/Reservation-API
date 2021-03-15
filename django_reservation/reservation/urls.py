from django.contrib import admin
from django.urls import path, include
from reservation.views import *
from rest_framework.authtoken.views import obtain_auth_token

app_name = "reservations"
urlpatterns = [
    path("auth/token", obtain_auth_token, name="token"),

    path("", include("djoser.urls")),
    path("", include("djoser.urls.authtoken")),
    path("restricted/", restricted),


    # path("meet/create/", MeetingCreateView.as_view()),
    path("meet/all/", MeetingListView.as_view()),
    path("meet/detail/<int:pk>/", MeetingDetailView.as_view()),
    # path("meet/test/", meeting_view),
    path("meet/read/", read, name="test1"),
    path("meet/read/<str:pk>", readbyid, name="testdetail"),
    path("meet/create/", create, name="testcreate"),
    path("meet/update/<str:pk>/", update, name="testcreate"),
    path("meet/delete/<str:pk>/", delete, name="testdelete"),

    path('rest-auth/', include('rest_auth.urls')),


]
