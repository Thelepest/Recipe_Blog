# Generated by Django 4.0.1 on 2022-02-01 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicazione', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='rating',
            field=models.FloatField(default=0.1),
        ),
    ]
