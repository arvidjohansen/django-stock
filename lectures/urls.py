from django.urls import path
from lectures.views import LectureDetailView


app_name = 'lectures'

urlpatterns = [
    path('<int:pk>', LectureDetailView.as_view(),name='detail'),
]