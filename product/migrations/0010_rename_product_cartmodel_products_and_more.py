# Generated by Django 4.0.4 on 2022-05-25 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_cartmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartmodel',
            old_name='product',
            new_name='products',
        ),
        migrations.RenameField(
            model_name='cartmodel',
            old_name='updeted_on',
            new_name='updated_on',
        ),
    ]