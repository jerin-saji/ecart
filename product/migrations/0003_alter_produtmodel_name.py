# Generated by Django 4.0.4 on 2022-05-04 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_unitmodel_conversion_ratio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtmodel',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
