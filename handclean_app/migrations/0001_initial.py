# Generated by Django 2.1 on 2020-04-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LyricModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
            ],
        ),
    ]