import os

from django.db import models

# Create your models here.


class Files(models.Model):
    title = models.CharField(max_length=80)
    pdf = models.FileField(upload_to='')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.pdf.name}"
    def filename(self):
        return os.path.basename(self.pdf.name)

