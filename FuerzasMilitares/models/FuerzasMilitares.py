from dataclasses import field, fields
from email.policy import default
from enum import auto, unique
from operator import ge
from tabnanny import verbose
from django.db import models
from django.core.management.utils import get_random_secret_key
from django.forms.widgets import HiddenInput
from django import forms


class FuerzasMilitares(models.Model):
    nombre = models.CharField(max_length=150, primary_key=True, unique=True)
    logo = models.ImageField(upload_to="images\\fuerzas_militares")
    token_acceso = models.CharField(
        max_length=255,
        default=get_random_secret_key,
        blank=True,
        null=True,
        editable=False,
        unique=True,
    )

    class Meta:
        verbose_name = "Fuerza Militar"
        verbose_name_plural = "Fuerzas Militares"

    def __str__(self) -> str:
        return f"{self.nombre}"
