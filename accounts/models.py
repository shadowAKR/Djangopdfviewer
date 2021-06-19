import os

from django.db import models

# Create your models here.


class Files(models.Model):
    pdf = models.FileField(upload_to='')

    class Meta:
        ordering = ['pdf']

    def __str__(self):
        return f"{self.pdf.name}"
    def filename(self):
        return os.path.basename(self.pdf.name)

