# Generated by Django 4.0.4 on 2022-05-26 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_contactus_is_replied'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='reply',
            field=models.TextField(default='no-reply', max_length=1000),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(max_length=1000),
        ),
    ]