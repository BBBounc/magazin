# Generated by Django 5.1.1 on 2024-09-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_portfolio_image_portfolioimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioimage',
            name='image',
            field=models.ImageField(upload_to='media/uploads/'),
        ),
    ]
