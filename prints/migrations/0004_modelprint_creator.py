# Generated by Django 4.0 on 2022-09-30 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('prints', '0003_manufacturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelprint',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='prints', to='users.customuser'),
            preserve_default=False,
        ),
    ]
