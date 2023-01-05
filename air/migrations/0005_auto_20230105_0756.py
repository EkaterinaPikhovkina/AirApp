# Generated by Django 3.2.12 on 2023-01-05 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0004_alter_city_api_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advice',
            name='pollutant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='air.pollutant', verbose_name='Забрудник'),
        ),
        migrations.AlterField(
            model_name='advice',
            name='prevention',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='air.prevention', verbose_name='Попередження'),
        ),
        migrations.AlterField(
            model_name='news',
            name='advice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='air.advice', verbose_name='Попередження'),
        ),
    ]
