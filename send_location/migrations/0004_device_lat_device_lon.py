# Generated by Django 4.2.5 on 2023-09-27 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('send_location', '0003_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='lat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lats', to='send_location.location'),
        ),
        migrations.AddField(
            model_name='device',
            name='lon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lons', to='send_location.location'),
        ),
    ]
