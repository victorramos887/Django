# Generated by Django 2.2.6 on 2022-12-12 16:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
        ('receitas', '0002_auto_20221212_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='pessoa',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pessoas.Pessoa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='receita',
            name='date_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 12, 16, 59, 31, 632201)),
        ),
        migrations.AlterField(
            model_name='receita',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]