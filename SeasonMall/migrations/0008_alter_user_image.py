# Generated by Django 4.0 on 2022-01-27 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SeasonMall', '0007_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
