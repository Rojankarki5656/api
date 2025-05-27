from django.urls import path
from .views import JobList, ApplicationCreate

urlpatterns = [
    path('jobs/', JobList.as_view(), name='job-list'),
    path('applications/', ApplicationCreate.as_view(), name='application-create'),
]