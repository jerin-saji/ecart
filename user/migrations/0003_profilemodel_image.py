# Generated by Django 4.0.4 on 2022-05-07 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profilemodel_age_profilemodel_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='image',
            field=models.ImageField(default='default/product.png', upload_to='image/user/'),
        ),
    ]