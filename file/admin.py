from django.contrib import admin
from .models import FileDownload
# Register your models here.

@admin.register(FileDownload)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "file_name"]