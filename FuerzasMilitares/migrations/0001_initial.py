# Generated by Django 4.1 on 2022-09-14 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FuerzasMilitares",
            fields=[
                (
                    "nombre",
                    models.CharField(
                        max_length=100, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("logo", models.ImageField(upload_to="images\\fuerzas_militares")),
            ],
            options={
                "verbose_name": "Fuerza Militar",
                "verbose_name_plural": "Fuerzas Militares",
            },
        ),
    ]