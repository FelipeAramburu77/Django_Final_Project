from django.db import models

# Create your models here.
class Locales(models.Model):
    name=models.CharField(max_length=50,default="")
    CITY = (
        (1, "Córdoba"),
        (2, "Capital Federal"),
        (3, "Rosario"),
        (4, "Mendoza"),
        (5, "Salta"),
        )
    city= models.PositiveSmallIntegerField("City",choices=CITY, default=1)
    address= models.CharField(max_length=50)
    mall_number= models.IntegerField()
    DAYS=(
        (1, "Monday to friday"),
        (2, "Monday to saturday"),
        (3, "Monday to monday"),
    )
    opening_hours=models.PositiveSmallIntegerField("Opening days",choices=DAYS, default=1)
    class Meta:
        verbose_name_plural = "Locales"

class Vendedores(models.Model):
    name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    email= models.EmailField()
    mall_number= models.CharField(max_length=30)
    birthday= models.DateField()
    class Meta:
        verbose_name_plural = "Vendedores"
    def __str__(self):
        return f"Name: {self.name} - Last name: {self.last_name} - Email: {self.email} - Mall number: {self.mall_number} - Birthday: {self.birthday}"

class Productos(models.Model):
    product= models.CharField(max_length=30)
    prize= models.FloatField("Prize $")
    marcas=(
        (1, 'Apple'),
        (2, 'Samsung'),
        (3, 'Huawei'),
        (4, 'Sony')
    )   
    brand= models.PositiveSmallIntegerField("Brand",choices=marcas)
    stock= models.IntegerField("Stock")
    class Meta:
        verbose_name_plural = "Productos"
        # con esta indicación comenzamos a ver detalladamente en nuestra BD

class Nuevos_Productos(models.Model):
    product= models.CharField(max_length=30)
    brand= models.CharField(max_length=30)
    release_date= models.DateField()
    class Meta:
        verbose_name_plural = "Nuevos Productos"
    def __str__(self):
        return f"Product: {self.product} - Brand: {self.brand} - Release date: {self.release_date}"



        