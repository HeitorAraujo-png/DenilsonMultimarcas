from django.db import models
from django.core.exceptions import ValidationError


class Roupa(models.Model):
    id = models.AutoField(auto_created=True, blank=False, primary_key=True)
    name = models.CharField(null=False, max_length=256)
    img = models.ImageField(upload_to='clothes/', blank=True)
    unit = models.PositiveIntegerField(blank=True, default=0)
    price = models.FloatField(blank=False, null=False)
    price_promo = models.FloatField(blank=True, null=True)
    is_promo = models.BooleanField(default=False, blank=False)
    
    def clean(self):
        if self.is_promo and self.price < self.price_promo:
            raise ValidationError('O preço promocional é maior que o preço comum!')
        return super().clean()
    