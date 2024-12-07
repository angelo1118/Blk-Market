from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=400)
    price = models.FloatField(max_length=10, default=0.0)
    image = models.ImageField(null=True, blank=True, upload_to="images/", default = "products/product-default.png")
    barcode = models.ImageField(upload_to='barcodes/', blank=True, null=True)

    def generate_barcode(self):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f"{self.pk:012}", writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save(f"{self.name}_barcode.png", File(buffer), save=False)
        buffer.close()

    def save(self, *args, **kwargs):
        if not self.barcode:
            self.generate_barcode()
        super().save(*args, **kwargs)
    
    

