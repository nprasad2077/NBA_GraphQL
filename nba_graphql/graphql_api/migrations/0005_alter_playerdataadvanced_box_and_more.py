# Generated by Django 4.2.7 on 2024-02-03 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("graphql_api", "0004_alter_playerdataadvanced_assist_percent_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="playerdataadvanced",
            name="box",
            field=models.DecimalField(
                blank=True, decimal_places=1, max_digits=6, null=True
            ),
        ),
        migrations.AlterField(
            model_name="playerdataadvanced",
            name="offensive_box",
            field=models.DecimalField(
                blank=True, decimal_places=1, max_digits=6, null=True
            ),
        ),
    ]
