# Generated by Django 4.0 on 2022-09-30 14:01

from django.db import migrations, models
import prints.models


class Migration(migrations.Migration):

    dependencies = [
        ('prints', '0006_alter_modelprint_filament'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelprint',
            name='filament',
            field=models.ForeignKey(on_delete=models.SET(prints.models.get_or_create_a_deleted_filament), related_name='prints', to='prints.filament'),
        ),
    ]