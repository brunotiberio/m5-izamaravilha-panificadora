# Generated by Django 4.1.2 on 2022-11-04 18:40

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
            name="Comanda",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("aberta", "Aberta"),
                            ("fechada", "Fechada"),
                            ("em rota de entrega", "Em Rota De Entrega"),
                            ("entregue", "Entregue"),
                        ],
                        default="aberta",
                        max_length=30,
                    ),
                ),
                ("data_criacao", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Comanda_Produto",
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
                ("quantidade", models.PositiveIntegerField()),
                (
                    "comanda",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comanda_produto",
                        to="comandas.comanda",
                    ),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comanda_produto",
                        to="produtos.produto",
                    ),
                ),
            ],
        ),
    ]
