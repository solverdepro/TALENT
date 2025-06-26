from django.db import models

# Create your models here.
class MediaUploaded(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/accepted', blank=True)
    video = models.FileField(upload_to='videos/acepted', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title