from django.db import models
from django.core.exceptions import ValidationError

  
class Clothe(models.Model):
    Id = models.AutoField(auto_created=True, blank=False, primary_key=True)
    Name = models.CharField(null=False, max_length=256, blank=False)
    Img = models.ImageField(upload_to='clothes_view/', blank=True)
    Unit = models.PositiveIntegerField(blank=False, null=False , default=0)
    Price = models.FloatField(blank=False, null=False)
    Price_promo = models.FloatField(blank=True, null=True)
    Is_promo = models.BooleanField(default=False, blank=False)
    Active = models.BooleanField(default=True, blank=False)
    
    def clean(self):
        if self.Is_promo and self.Price < self.Price_promo:
            raise ValidationError('O preço promocional é maior que o preço comum!')
        if not self.Is_promo and self.Price_promo:
            self.Price_promo = None
        return super().clean()

class Category(models.Model):
    Id = models.AutoField(auto_created=True, blank=False, primary_key=True)
    Name = models.CharField(null=False, max_length=150, blank=False)
    Active = models.BooleanField(default=True, blank=False)
    
    def clean(self):
        if Category.objects.filter(Name=self.Name).exists():
            raise ValidationError("Já existe uma categoria de roupa com esse nome")
        return super().clean()

class ClotheImage(models.Model):
    Id = models.AutoField(auto_created=True, blank=False, primary_key=True)
    Img = models.ImageField(upload_to='clothes/', blank=True)
    Fk_clothe = models.ForeignKey(Clothe, null=False, on_delete=models.CASCADE)
    
    
    
class Description(models.Model): 
    Id = models.AutoField(auto_created=True, blank=False, primary_key=True)
    Text = models.TextField(null=False, blank=False)
    Size = models.CharField(null=False, max_length=4, blank=False)
    Specification = models.TextField(null=False, blank=False)
    Mark = models.CharField(null=False, blank=False)
    Fk_category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    Fk_clothe = models.ForeignKey(Clothe, null=False, blank=False, on_delete=models.CASCADE)
