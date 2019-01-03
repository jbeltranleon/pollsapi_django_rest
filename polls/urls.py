from django.urls import path
from views import polls_list, polls_detail

urlpatterns = [
    path("polls/", polls_list, name="list"),
    path("polls/<int:pk>/", polls_detail, name="detail")
]