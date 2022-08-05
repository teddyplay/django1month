from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Название',max_length=100)

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField('Название',max_length=100)

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 null=True)
    tags = models.ManyToManyField(Tag,blank=True)
    name = models.CharField(max_length=100) #название
    description = models.TextField(blank=True) #описание
    price = models.FloatField() #цена
    is_active = models.BooleanField() #активен ли товар
    created_ad = models.DateTimeField(auto_now_add=True) #дата создания
    update_ad = models.DateTimeField(auto_now=True) #дата обновления

    def __str__(self):
        return self.name


