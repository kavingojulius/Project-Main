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
    
    def delete(self, using=None, keep_parents=False):
        self.name.delete()
        super().delete()
    
    class Meta:
        verbose_name_plural = 'Video work'


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images_uploaded')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Service'

class HeroSection(models.Model):        
    image = models.ImageField(upload_to='hero_images')
    description = models.TextField()

    def __str__(self):
        return 'image'
    
    class Meta:
        verbose_name_plural = 'Hero Section'
