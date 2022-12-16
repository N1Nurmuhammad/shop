from django.db import models
from app.models import AdModel
# from accounts.models.account import Account

class CountryModel(models.Model):
    region = models.CharField(max_length=255, blank=True, null=True)
    distict = models.CharField(max_length=255, blank=True, null=True)
    ad = models.ForeignKey(AdModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='country',)


    def __str__(self):
        return str(self.region)

    # class Meta:
    #     app_label = "accounts"