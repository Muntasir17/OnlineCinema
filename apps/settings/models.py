from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=250)
    decription = models.TextField()
    logo = models.ImageField(upload_to = 'logo/')
    tel = models.CharField(max_length=255)
    email = models.EmailField()
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    google = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    pinterest = models.CharField(max_length=255)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

# class About(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     owner = models.CharField(max_length=255)
#     position = models.CharField(max_length=100)
#     signature = models.ImageField(upload_to = "signature/")

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = "О нас"
#         verbose_name_plural = "О нас"