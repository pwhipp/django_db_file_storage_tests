from django.db import models


class FileUploader(models.Model):
    upload = models.FileField()
