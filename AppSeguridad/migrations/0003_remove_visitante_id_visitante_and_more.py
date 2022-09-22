# Generated by Django 4.1 on 2022-09-22 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("AppSeguridad", "0002_remove_modeloinstalacion_id_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="visitante",
            name="id_visitante",
        ),
        migrations.AlterField(
            model_name="visitante",
            name="datosbasicos_ptr",
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to="AppSeguridad.datosbasicos",
            ),
        ),
    ]