# Generated by Django 4.0 on 2022-10-03 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prints', '0003_alter_modelprint_filament_instance'),
    ]

    operations = [
        migrations.AddField(
            model_name='filamentroll',
            name='manufacturer',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]