from django.db import models

# Create your models here.

class ImagesWork(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images_uploaded')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Image work'

class VideosWork(models.Model):
    name = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos_uploaded')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Video work'