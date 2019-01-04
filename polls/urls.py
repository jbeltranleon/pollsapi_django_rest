from django.urls import path
from .apiviews import PollList, PollDetail

urlpatterns = [
    path("polls/", PollList.as_view(), name="list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="detail")
]