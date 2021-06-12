from django.db import models


class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    contributor = models.CharField(max_length=30)
    user_image = models.ImageField(upload_to="")  # upload_to は画像の置き場を指定する。置き場の基準はsettings.pyで指定している。
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.TextField(null=True, blank=True, default="")
