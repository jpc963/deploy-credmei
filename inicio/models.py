from django.db import models


class Cep(models.Model):
    cep = models.CharField(max_length=8, blank=False, null=False)
    state = models.CharField(max_length=30, blank=True, null=False)
    city = models.CharField(max_length=30, blank=True, null=False)
    neighborhood = models.CharField(max_length=30, blank=True, null=False)
    street = models.CharField(max_length=30, blank=True, null=False)
    service = models.CharField(max_length=15, blank=True, null=False)

    def __str__(self):
        return self.cep
