# Generated by Django 2.1 on 2020-04-15 17:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('handclean_app', '0002_reviewmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewmodel',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2020, 4, 15, 17, 41, 54, 608710, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='picture',
            field=models.ImageField(upload_to='posters_review'),
        ),
    ]