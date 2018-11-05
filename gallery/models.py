from django.db import models
import datetime as dt

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    verbose_name_plural = "Categories"

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to ='images/',blank=True)
    image_name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 50)
    image_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        photos = cls.objects.filter(pub_date__date = today)
        return photos

 

    @classmethod
    def search_by_image_category(cls,search_term):
        photos = cls.objects.filter(image_category__name=search_term)
        return photos

        