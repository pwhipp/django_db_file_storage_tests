from django.test import TestCase
from django.core.files.base import ContentFile

from file_uploader.models import FileUploader


class TestFileUploader(TestCase):
    def test_file_uploader(self):
        file_name = 'test.txt'
        file_content_string = 'Test file content'
        file_content = ContentFile(file_content_string)

        uploader = FileUploader()
        uploader.upload.save(file_name, file_content)
        uploader.save()
        uploader_id = uploader.id

        new_uploader = FileUploader.objects.get(id=uploader_id)
        new_uploader.upload.open('r')
        new_uploader_file_content_string = new_uploader.upload.read()
        new_uploader.upload.close()

        self.assertEqual(file_content_string, new_uploader_file_content_string)

