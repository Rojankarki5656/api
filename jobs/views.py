from rest_framework import generics
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer

class JobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class ApplicationCreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer