# Generated by Django 4.0 on 2022-10-02 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prints', '0002_alter_modelprint_filament_instance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelprint',
            name='filament_instance',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='print', to='prints.filamentinstance'),
        ),
    ]