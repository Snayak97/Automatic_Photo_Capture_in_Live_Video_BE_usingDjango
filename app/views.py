from django.shortcuts import render

# Create your views here.

from app.models import *
from app.serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser


class PhotoUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request):
        photos = Photo.objects.all().order_by('-created_at').first()
        # photos = Photo.objects.all()
        serializer = PhotoSerializer(photos)
        return Response(serializer.data)

