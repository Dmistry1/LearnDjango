from django.db import models

# Create your models here.
class CatFacts(models.model):
    text = models.TextField()
    image_url = models.TextField()