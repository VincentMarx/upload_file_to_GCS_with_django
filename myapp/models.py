from django.db import models

# Create your models here.

class Document(models.Model):
    docfile = models.FileField(upload_to='')
    filename = models.Field()
    uploadedby = models.Field()
    lastuploadtime = models.DateTimeField()

    def __str__(self):
        return self.filename