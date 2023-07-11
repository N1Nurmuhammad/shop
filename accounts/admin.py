from django.contrib import admin
from accounts.models import Account, UserContactsModel
from accounts.models import CountryModel, PrivacyModel

admin.site.register(Account)
admin.site.register(CountryModel)
admin.site.register(PrivacyModel)
admin.site.register(UserContactsModel)
