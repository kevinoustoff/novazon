# Generated by Django 4.2.2 on 2023-06-27 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relais', '0012_alter_pointrelais_quartier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointrelais',
            name='quartier',
            field=models.CharField(max_length=300),
        ),
    ]
