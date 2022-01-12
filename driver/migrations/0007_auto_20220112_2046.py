# Generated by Django 3.2.9 on 2022-01-12 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('driver', '0006_auto_20220112_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='customer',
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rating',
            name='avarage_rate',
            field=models.IntegerField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='efficiency_rate',
            field=models.IntegerField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='service_rate',
            field=models.IntegerField(blank=True, default=0, max_length=10, null=True),
        ),
    ]