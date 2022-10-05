# Generated by Django 4.1 on 2022-10-05 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("FuerzasMilitares", "0002_alter_practicapoligono_table"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="arma",
            options={"verbose_name": "Arma", "verbose_name_plural": "Armas"},
        ),
        migrations.AlterModelOptions(
            name="modeloarma",
            options={},
        ),
        migrations.AlterModelTable(
            name="arma",
            table="arma",
        ),
        migrations.AlterModelTable(
            name="datosbasicos",
            table="datos_basicos",
        ),
        migrations.AlterModelTable(
            name="divisionmilitar",
            table="division_militar",
        ),
        migrations.AlterModelTable(
            name="fuerzamilitar",
            table="fuerza_militar",
        ),
        migrations.AlterModelTable(
            name="instalacionmilitar",
            table="instalacion_militar",
        ),
        migrations.AlterModelTable(
            name="militar",
            table="militar",
        ),
        migrations.AlterModelTable(
            name="modeloarma",
            table="modelo_arma",
        ),
        migrations.AlterModelTable(
            name="modeloinstalacion",
            table="modelo_instalacion",
        ),
    ]
