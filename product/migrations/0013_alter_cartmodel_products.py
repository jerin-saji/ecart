# Generated by Django 4.0.4 on 2022-05-25 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_cartmodel_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmodel',
            name='products',
            field=models.ManyToManyField(blank=True, to='product.productmodel'),
        ),
    ]