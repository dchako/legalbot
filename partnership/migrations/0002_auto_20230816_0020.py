# Generated by Django 3.2.7 on 2023-08-16 03:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnership',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 16, 0, 20, 6, 213142)),
        ),
        migrations.AlterField(
            model_name='partnership',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
