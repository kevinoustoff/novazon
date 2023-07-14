# Generated by Django 4.2.2 on 2023-06-27 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relais', '0003_alter_pointrelais_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointrelais',
            name='gmanager_signature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pointrelais',
            name='relay_name',
            field=models.CharField(default='non renseigné', max_length=100),
        ),
        migrations.AlterField(
            model_name='pointrelais',
            name='key',
            field=models.CharField(default='L19CTKJZ50', max_length=10, unique=True),
        ),
    ]
