from django.db import models
from datetime import datetime


# Create your models here.
class Partnership(models.Model):
    ''' Class to represent the partnership. '''

    name = models.CharField(max_length=50, unique=True)
    rut = models.CharField(max_length=9)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Partner(models.Model):
    ''' Class to represent the partner. '''

    name = models.CharField(max_length=50, unique=True)
    rut = models.CharField(max_length=9)
    entry = models.PositiveIntegerField(default=0, )
    address = models.CharField(max_length=129)
    partnership = models.ManyToManyField(Partnership, related_name='partners')


class Manager(models.Model):
    ''' Class to represent the manager. '''

    name = models.CharField(max_length=50, unique=True)
    rut = models.CharField(max_length=9)
    capacity = models.CharField(
        max_length=30,
        choices=(
            ("abrir una cuenta corriente", "abrir una cuenta corriente"),
            ("firmar cheques", "firmar cheques"),
            ("firmar contratos", "firmar contratos")
        ),
        default="nominativas")
    partnership = models.ManyToManyField(Partnership, related_name='managers')
