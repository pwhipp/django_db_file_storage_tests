from django.db import models


class FileUploader(models.Model):
    upload = models.FileField(upload_to='file_uploader.DBFile/bytes/filename/mimetype',
                              blank=True,
                              null=True)


class DBFile(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)