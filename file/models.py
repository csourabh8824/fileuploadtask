from django.db import models


class FileDownload(models.Model):
    name = models.CharField(max_length=20)
    file_name = models.FileField(upload_to='static/pdfs/')
