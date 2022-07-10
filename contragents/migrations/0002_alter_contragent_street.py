# Generated by Django 3.2.8 on 2022-07-10 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_street'),
        ('contragents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contragent',
            name='street',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='addresses.street', verbose_name='Street'),
        ),
    ]