# Generated by Django 4.1 on 2022-08-24 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("AppSeguridad", "0002_arma_alter_datospersonales_copia_cedula_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArmaNoLetal",
            fields=[
                (
                    "arma_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        to="AppSeguridad.arma",
                    ),
                ),
                (
                    "id_arma_no_letal",
                    models.AutoField(primary_key=True, serialize=False),
                ),
            ],
            bases=("AppSeguridad.arma",),
        ),
    ]
