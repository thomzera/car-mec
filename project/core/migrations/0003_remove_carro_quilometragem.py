# Generated by Django 4.1.3 on 2022-11-20 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_carro_ano"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="carro",
            name="quilometragem",
        ),
    ]
