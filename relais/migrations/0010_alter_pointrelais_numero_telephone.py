# Generated by Django 4.2.2 on 2023-06-27 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relais', '0009_pointrelais_numero_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointrelais',
            name='numero_telephone',
            field=models.CharField(max_length=8),
        ),
    ]