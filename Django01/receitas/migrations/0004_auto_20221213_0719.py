# Generated by Django 2.2.6 on 2022-12-13 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_auto_20221212_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='receita',
            name='date_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 13, 7, 19, 49, 952639)),
        ),
    ]
