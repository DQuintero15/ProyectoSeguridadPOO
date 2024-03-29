# Generated by Django 4.1 on 2022-10-12 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("FuerzasMilitares", "0006_remove_poligono_fecha_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="practicapoligono",
            name="militar",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="practica_militar",
                to="FuerzasMilitares.militar",
            ),
        ),
        migrations.AlterField(
            model_name="poligono",
            name="cartuchos",
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name="poligono",
            name="practica_poligono",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"disponible": True},
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="poligono_practica",
                to="FuerzasMilitares.practicapoligono",
            ),
        ),
        migrations.AlterField(
            model_name="poligono",
            name="provedores",
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name="practicapoligono",
            name="modelo_objetivo",
            field=models.ImageField(blank=True, null=True, upload_to="images\\modelos"),
        ),
    ]
