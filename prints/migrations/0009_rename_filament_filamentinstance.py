# Generated by Django 4.0 on 2022-10-02 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prints', '0008_alter_modelprint_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Filament',
            new_name='FilamentInstance',
        ),
    ]
