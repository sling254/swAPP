# Generated by Django 3.2.9 on 2022-01-12 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
