# Generated by Django 4.1 on 2022-11-08 04:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("AppSeguridad", "0003_alter_modelovisitante_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="visitante",
            name="datos_entrada",
            field=models.DateTimeField(
                default=django.utils.timezone.now, editable=False
            ),
        ),
        migrations.AddField(
            model_name="visitante",
            name="motivo",
            field=models.TextField(default="No presenta motivo", max_length=300),
        ),
    ]