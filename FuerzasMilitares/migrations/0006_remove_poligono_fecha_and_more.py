# Generated by Django 4.1 on 2022-10-10 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "FuerzasMilitares",
            "0005_remove_modeloinstalacion_ubicacion_latitud_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="poligono",
            name="fecha",
        ),
        migrations.RemoveField(
            model_name="practicapoligono",
            name="militar",
        ),
        migrations.RemoveField(
            model_name="practicapoligono",
            name="poligono",
        ),
        migrations.AddField(
            model_name="poligono",
            name="practica_poligono",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="poligono_practica",
                to="FuerzasMilitares.practicapoligono",
            ),
        ),
        migrations.AddField(
            model_name="practicapoligono",
            name="disponible",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="practicapoligono",
            name="fecha",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="practicapoligono",
            name="modelo_objetivo",
            field=models.ImageField(blank=True, null=True, upload_to="images\\modelo"),
        ),
        migrations.AlterField(
            model_name="poligono",
            name="distancia",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="poligono",
            name="id_poligono",
            field=models.AutoField(
                default=0, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
