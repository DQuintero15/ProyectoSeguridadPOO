# Generated by Django 4.1 on 2022-09-22 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("FuerzasMilitares", "0003_modeloarma_fuerza_militar"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="modeloarma",
            name="fuerza_militar",
        ),
        migrations.AddField(
            model_name="arma",
            name="fuerza_militar",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="modelo_arma_fuerza_militar",
                to="FuerzasMilitares.fuerzamilitar",
            ),
        ),
    ]