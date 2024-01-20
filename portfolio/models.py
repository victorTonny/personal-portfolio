from django.db import models

# Create your models here.
# portfolio/models.py

from django.db import models

class Project(models.Model):
    project_title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='projects/thumbnails/')
    description = models.TextField()

    def __str__(self):
        return self.project_title


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.subject
