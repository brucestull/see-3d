# Generated by Django 4.0 on 2022-10-01 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prints', '0007_alter_modelprint_filament'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelprint',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name of 3D Print Model'),
        ),
    ]