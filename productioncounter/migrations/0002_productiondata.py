# Generated by Django 5.0.6 on 2024-05-31 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productioncounter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(max_length=255)),
                ('order', models.CharField(max_length=255)),
                ('lot_number', models.CharField(max_length=255)),
                ('hour', models.IntegerField()),
                ('total_production_hour', models.IntegerField()),
                ('total_production', models.IntegerField()),
                ('fail_count', models.IntegerField()),
            ],
        ),
    ]
