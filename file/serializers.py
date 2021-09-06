from .models import  FileDownload
from rest_framework import serializers


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileDownload
        fields = ["name", "file_name"]