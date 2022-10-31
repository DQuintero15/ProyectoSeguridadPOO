# Generated by Django 4.1 on 2022-10-15 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("FuerzasMilitares", "0008_poligono_militar"),
    ]

    operations = [
        migrations.AddField(
            model_name="poligono",
            name="n_impactos",
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name="poligono",
            name="prom_efectividad",
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]