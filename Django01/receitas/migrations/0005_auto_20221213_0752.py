# Generated by Django 2.2.6 on 2022-12-13 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0004_auto_20221213_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='date_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 13, 7, 52, 14, 794747)),
        ),
    ]
