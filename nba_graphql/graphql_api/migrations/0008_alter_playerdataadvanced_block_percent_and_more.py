# Generated by Django 4.2.7 on 2024-02-03 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("graphql_api", "0007_alter_playerdataadvanced_usage_percent_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="playerdataadvanced",
            name="block_percent",
            field=models.DecimalField(
                blank=True, decimal_places=3, max_digits=6, null=True
            ),
        ),
        migrations.AlterField(
            model_name="playerdataadvanced",
            name="ftr",
            field=models.DecimalField(
                blank=True, decimal_places=3, max_digits=6, null=True
            ),
        ),
        migrations.AlterField(
            model_name="playerdataadvanced",
            name="steal_percent",
            field=models.DecimalField(
                blank=True, decimal_places=3, max_digits=6, null=True
            ),
        ),
        migrations.AlterField(
            model_name="playerdataadvanced",
            name="three_p_ar",
            field=models.DecimalField(
                blank=True, decimal_places=3, max_digits=6, null=True
            ),
        ),
        migrations.AlterField(
            model_name="playerdataadvanced",
            name="ts_percent",
            field=models.DecimalField(
                blank=True, decimal_places=3, max_digits=6, null=True
            ),
        ),
        migrations.AlterField(
            model_name="playerdataadvanced",
            name="vorp",
            field=models.DecimalField(
                blank=True, decimal_places=1, max_digits=6, null=True
            ),
        ),
    ]
