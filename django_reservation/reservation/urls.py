# local library
from reservation.views import *

# Django
from django.contrib import admin
from django.urls import path, include

# Third-party
from rest_framework.authtoken.views import obtain_auth_token

app_name = "reservations"
urlpatterns = [
    path("auth/token", obtain_auth_token, name="token"),
    path('rest-auth/', include('rest_auth.urls')),

    path("", include("djoser.urls")),
    path("", include("djoser.urls.authtoken")),
    path("restricted/", restricted),


    path("meet/create/", MeetingCreateView.as_view()),
    path("meet/all/", MeetingListView.as_view()),
    path("meet/detail/<int:pk>/", MeetingDetailView.as_view()),

    path("meet/read/", read),
    path("meet/read/<str:pk>", readbyid),

    path("meet/update/<str:pk>/", update),
    path("meet/delete/<str:pk>/", delete)

]
