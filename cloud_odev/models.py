from django.db import models

class Kisi(models.Model):
    KisiMail = models.EmailField(unique=True)
    KisiPassword = models.CharField(max_length=20)