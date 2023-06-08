from django.db import models
from avtoelon import settings
from uuid import uuid4


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'ads/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class AdLocationModel(models.Model):
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)

    ad = models.ForeignKey("AdModel", on_delete=models.SET_NULL, null=True, blank=True, related_name='location', )

    def __str__(self):
        return f"{self.ad} - {self.longitude} - {self.latitude}"


class AdPictureModel(models.Model):
    picture = models.ImageField(upload_to=upload_location, null=True, blank=True)
    ad = models.ForeignKey('AdModel', on_delete=models.SET_NULL, null=True, blank=True, related_name='picture', )


class CategoriesModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SubCategoriesModel(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(CategoriesModel, related_name='subcategory', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class AdModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ads', on_delete=models.SET_NULL, blank=True,
                              null=True)
    # picture = models.ForeignKey(AdPicturModel, on_delete=models.CASCADE, null=True, blank=True)
    price = models.PositiveIntegerField()
    state = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(CategoriesModel, on_delete=models.SET_NULL, null=True, blank=True)
    subcategory = models.ForeignKey(SubCategoriesModel, on_delete=models.SET_NULL, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    model = models.CharField(max_length=255, null=True, blank=True)
    # country = models.ForeignKey(AdLocationModel, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=255, null=True, blank=True)
    seen = models.IntegerField(default=0)
    ram = models.IntegerField()
    memory = models.IntegerField()
    discount_price = models.IntegerField()

    def __str__(self):
        return str(self.model)


class FavAdModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='favs', on_delete=models.SET_NULL, blank=True,
                              null=True)
    ad = models.ForeignKey(AdModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.owner} - {self.ad}"

    class Meta:
        unique_together = ['owner', 'ad']
