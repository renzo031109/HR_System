# Generated by Django 5.0.6 on 2024-11-13 16:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiving_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
