# Generated by Django 4.1 on 2022-09-14 15:17

import django.core.management.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("FuerzasMilitares", "0004_alter_fuerzasmilitares_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="fuerzasmilitares",
            options={
                "verbose_name": "Fuerza Militar",
                "verbose_name_plural": "Fuerzas Militares",
            },
        ),
        migrations.AlterField(
            model_name="fuerzasmilitares",
            name="nombre",
            field=models.CharField(
                max_length=150, primary_key=True, serialize=False, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="fuerzasmilitares",
            name="token_acceso",
            field=models.CharField(
                blank=True,
                default=django.core.management.utils.get_random_secret_key,
                editable=False,
                max_length=255,
                null=True,
            ),
        ),
    ]