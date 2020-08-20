# Generated by Django 3.1 on 2020-10-11 10:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_uerdet'),
        ('products', '0013_auto_20201001_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('product_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.uerdet')),
            ],
        ),
    ]
