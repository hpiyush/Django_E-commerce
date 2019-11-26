from django.db import models
from PIL import Image

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=12, default='untitnled', blank=False, null=False)
    description = models.TextField(max_length=5000)
    price = models.FloatField(max_length=12)
    availability = models.IntegerField()
    image = models.ImageField(default='default.jpeg', upload_to='product_pics')


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        # if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)