# Generated by Django 4.1.2 on 2022-11-07 12:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("produtos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Estoque",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("quantidade", models.IntegerField()),
                ("atualizado_em", models.DateTimeField(auto_now=True)),
                (
                    "produto",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="estoque",
                        to="produtos.produto",
                    ),
                ),
            ],
        ),
    ]
