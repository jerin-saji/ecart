# Generated by Django 4.0.4 on 2022-05-05 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_produtmodel_created_on_produtmodel_status_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Produtmodel',
            new_name='ProductModel',
        ),
    ]
