from django.db import models


class EdcModule(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    order_number = models.IntegerField(unique=True, null=True)

    def __str__(self):
        return self.name

