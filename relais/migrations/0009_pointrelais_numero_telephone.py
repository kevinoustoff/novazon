# Generated by Django 4.2.2 on 2023-06-27 02:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('relais', '0008_alter_pointrelais_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointrelais',
            name='numero_telephone',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
