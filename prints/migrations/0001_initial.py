# Generated by Django 4.0 on 2022-10-07 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilamentInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filament_consumed', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FilamentRoll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=255)),
                ('material', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ModelPrint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name of 3D Print Model')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prints', to='users.customuser')),
                ('filament_instance', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='print', to='prints.filamentinstance')),
            ],
        ),
        migrations.AddField(
            model_name='filamentinstance',
            name='filament_roll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prints.filamentroll'),
        ),
    ]
