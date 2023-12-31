# Generated by Django 4.2.4 on 2023-08-14 17:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0003_add_slug_to_project"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="zip_code",
            field=models.PositiveIntegerField(
                default=501,
                validators=[
                    django.core.validators.MinValueValidator(501),
                    django.core.validators.MaxValueValidator(999999999),
                ],
            ),
            preserve_default=False,
        ),
    ]
