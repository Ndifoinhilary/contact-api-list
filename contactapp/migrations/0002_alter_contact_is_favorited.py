# Generated by Django 4.2.3 on 2023-07-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='is_favorited',
            field=models.BooleanField(default=False),
        ),
    ]