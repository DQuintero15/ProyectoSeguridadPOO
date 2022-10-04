# Generated by Django 4.1 on 2022-10-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("FuerzasMilitares", "0003_remove_ubicacionmilitar_batallon_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="brigadamilitar",
            name="division",
        ),
        migrations.RemoveField(
            model_name="brigadamilitar",
            name="modeloinstalacion_ptr",
        ),
        migrations.AddField(
            model_name="instalacionmilitar",
            name="logo",
            field=models.ImageField(blank=True, null=True, upload_to="images\\logos"),
        ),
        migrations.DeleteModel(
            name="Batallon",
        ),
        migrations.DeleteModel(
            name="BrigadaMilitar",
        ),
    ]
