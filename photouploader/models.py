from django.db import models
from django.db.models.fields import TextField
from sorl.thumbnail import ImageField

# Create your models here.
class PostPhoto(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    caption = TextField()
    image = ImageField()

    def __str__(self) -> str:
        return self.title