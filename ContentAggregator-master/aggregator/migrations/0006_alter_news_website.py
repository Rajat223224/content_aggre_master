# Generated by Django 3.2.7 on 2021-09-29 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0005_auto_20210929_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='website',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aggregator.website'),
        ),
    ]