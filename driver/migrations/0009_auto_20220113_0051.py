# Generated by Django 3.2.9 on 2022-01-12 21:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0008_rename_user_rating_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='customer',
        ),
        migrations.AlterField(
            model_name='rating',
            name='avarage_rate',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='driver.driver'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='efficiency_rate',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='service_rate',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
