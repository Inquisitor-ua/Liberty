# Generated by Django 5.0.6 on 2025-02-25 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_otzuvu_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otzuvu',
            name='data',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
    ]
