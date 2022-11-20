# Generated by Django 4.1.3 on 2022-11-19 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MarcaCarro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name="Carro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=24)),
                ("ano", models.DateField()),
                ("quilometragem", models.FloatField()),
                (
                    "marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.marcacarro",
                    ),
                ),
            ],
            options={
                "ordering": ["nome"],
            },
        ),
    ]