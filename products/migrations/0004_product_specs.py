# Generated by Django 3.1 on 2020-08-14 10:03

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200814_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specs',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
    ]
