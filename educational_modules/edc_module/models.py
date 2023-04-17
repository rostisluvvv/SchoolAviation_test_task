from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class EdcModule(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    order_number = models.IntegerField(unique=True)


@receiver(pre_save, sender=EdcModule)
def set_order_number(sender, instance, **kwargs):
    if not instance.order_number:
        last_module = EdcModule.objects.order_by('-order_number').first()
        instance.order_number = last_module.order_number + 1 if last_module else 1
