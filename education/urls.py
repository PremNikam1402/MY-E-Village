from django.urls import path
from .views import CourseListView, EnrollView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='courses'),
    path('enroll/', EnrollView.as_view(), name='enroll'),
]