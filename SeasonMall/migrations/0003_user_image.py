# Generated by Django 4.0 on 2022-01-27 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SeasonMall', '0002_product_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='/media/uploads/SM.png', null=True, upload_to='uploads/'),
        ),
    ]
