from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class UserProfile(models.Model):
    DELIVERY_CHOICES = [
        ('cargus', 'Cargus'),
        ('sameday', 'Sameday'),
        ('pickup', 'Ridicare personală'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='userprofile'
    )
    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)
    delivery_method = models.CharField(
        max_length=20,
        choices=DELIVERY_CHOICES,
        default='cargus'
    )
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username
