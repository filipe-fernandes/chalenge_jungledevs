# Generated by Django 3.0.7 on 2021-02-27 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='url_name',
            field=models.SlugField(max_length=30, unique=True),
        ),
    ]
