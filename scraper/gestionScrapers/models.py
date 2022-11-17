from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model): 
    day = timezone.now()
    formatedDay  = day.strftime("%d/%m/%Y")

    id = models.AutoField(primary_key = True)
    page = models.CharField("Página", null=False, max_length=50)
    title = models.CharField("Producto-Titulo",max_length=300, null=False)
    price = models.IntegerField("Precio", null=False)
    link = models.CharField("Link",max_length=1000,null=True, blank=True)
    #dateFormat = models.DateTimeField(max_length=50, default=formatedDay)