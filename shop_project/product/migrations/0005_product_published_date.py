# Generated by Django 2.1.7 on 2019-10-03 06:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20191003_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
