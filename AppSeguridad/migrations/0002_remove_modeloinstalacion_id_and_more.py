# Generated by Django 4.1 on 2022-09-22 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppSeguridad", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="modeloinstalacion",
            name="id",
        ),
        migrations.AddField(
            model_name="modeloinstalacion",
            name="id_modelo_instalacion",
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
