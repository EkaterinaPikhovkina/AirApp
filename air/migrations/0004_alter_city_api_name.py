# Generated by Django 3.2.12 on 2023-01-05 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0003_auto_20230104_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='api_name',
            field=models.CharField(max_length=30, null=True, verbose_name='Назва для API'),
        ),
    ]
