from django.db import models


# Create your models here.

class TradingSymbol(models.Model):
    nse_name = models.CharField(max_length=255, blank=False)
    nse_symbol = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.nse_name
