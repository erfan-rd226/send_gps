# Generated by Django 4.2.5 on 2023-09-21 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SendLocationModel',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('timestamp', models.TimeField()),
                ('lat', models.CharField(max_length=50)),
                ('lon', models.CharField(max_length=50)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'send_location',
            },
        ),
    ]