from django.db import models
from django.urls import reverse
from shop.settings import AUTH_USER_MODEL

# Create your models here.
class Produit(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="articles", blank=True, null=True)
    
    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('produit', kwargs={'slug': self.slug})


class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.produit.name} ({self.quantity})"
    
class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateField(blank=True, null=True)

    def __str__(self):
         return self.user.username

    



