# Generated by Django 4.0.1 on 2022-02-03 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicazione', '0003_recipe_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='immagine',
            field=models.ImageField(default='templates/applicazione/default_pic.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='Add a description', max_length=200),
        ),
    ]
