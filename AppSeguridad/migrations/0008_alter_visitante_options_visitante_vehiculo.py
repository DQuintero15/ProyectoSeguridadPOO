# Generated by Django 4.1 on 2022-09-22 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "AppSeguridad",
            "0007_esquemaseguridad_batallon_esquemaseguridad_brigada_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="visitante",
            options={"verbose_name": "Visitante", "verbose_name_plural": "Visitantes"},
        ),
        migrations.AddField(
            model_name="visitante",
            name="vehiculo",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="visitante_vehiculo",
                to="AppSeguridad.vehiculo",
            ),
        ),
    ]
