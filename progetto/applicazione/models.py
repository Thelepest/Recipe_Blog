from django.db import models

# Create your models here.

class recipe(models.Model):
    immagine = models.ImageField()
    recipe = models.CharField(max_length=50)
    origin = models.CharField(max_length=20)
    rating = models.FloatField(default=0.1)
    description = models.TextField(max_length=200,default="Add a description")

    def __str__(self):
        return self.recipe
    #WITH THAT FUNCTION THE FIELD ON THE ADMIN PAGE RECEIVES THE RECIPE NAME


