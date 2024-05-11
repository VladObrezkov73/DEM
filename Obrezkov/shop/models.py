from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        
    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=7) #12345,67 всего 7 после запятой.после запятой 2 
    image = models.ImageField(null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)


    def __str__(self):
        return f"{self.name} - {self.price} - {self.category.name}"