# Generated by Django 2.1 on 2020-04-15 20:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('handclean_app', '0004_auto_20200415_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='date_posted',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]