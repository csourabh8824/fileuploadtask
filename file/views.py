from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class FileDownload(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request,format=None):
        print("get")
        serializer = FileSerializer()
        return Response(serializer.data)

    def post(self, request, format=None):
        python_data = request.data
        serializer = FileSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)