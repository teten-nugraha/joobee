from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import JobSerializer
from .models import Job

@api_view(['GET'])
def getAllJobs(request):

    jobs = Job.objects.all()

    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getJob(request, pk):
    job = get_object_or_404(Job, id=pk)

    serializer = JobSerializer(job, many=False)

    return Response(serializer.data)