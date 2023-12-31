# Generated by Django 4.2.2 on 2023-06-27 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relais', '0002_remove_pointrelais_created_at_pointrelais_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointrelais',
            name='latitude',
            field=models.DecimalField(decimal_places=20, max_digits=100),
        ),
        migrations.AlterField(
            model_name='pointrelais',
            name='longitude',
            field=models.DecimalField(decimal_places=20, max_digits=100),
        ),
    ]
