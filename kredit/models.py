from django.db import models
from django.dispatch import receiver
from accounts.models import Account
from django.db.models.signals import post_save
import requests
from django.http import Http404
from urllib.error import HTTPError
from decouple import config

SMS_AUTH_TOKEN = config('SMS_AUTH_TOKEN')
SMS_URL = config('SMS_URL')

CREDIT_STATUS_CHOICES = (
    ('ON HOLD', 'ON HOLD'),
    ('ACCEPTED', 'ACCEPTED'),
    ('IGNORED', 'IGNORED'),
)


class CreditModel(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    passport_seria = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    f_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    pinfl = models.CharField(max_length=255)
    status = models.CharField(choices=CREDIT_STATUS_CHOICES, max_length=55)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.l_name} - {self.passport_seria} - {self.pinfl} - {self.created_date}'


@receiver(post_save, sender=CreditModel)
def send_message(sender, instance=None, created=False, **kwargs):
    if instance.status == "ACCEPTED":
        header = {'Authorization': 'Bearer ' + SMS_AUTH_TOKEN}
        text = f'Your ariza na rastrochku accepted'
        data = {
            'mobile_phone': f'{instance.account.phone_number}',
            'message': f'{text}',
            'from': '4546',
            'callback_url': 'http://0000.uz/test.php'
        }

        try:
            r = requests.post(SMS_URL, json=data, headers=header)
        except HTTPError:
            raise Http404
