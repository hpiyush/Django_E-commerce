from django.db import models
from PIL import Image

# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Catagories"

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=50, default='Product', blank=False, null=False)
    description = models.TextField(max_length=5000)
    price = models.FloatField(max_length=12)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(default='default.jpeg', upload_to='product_pics')
    available = models.IntegerField(default=10)
    offer = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)