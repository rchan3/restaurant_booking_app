# Generated by Django 2.2.6 on 2019-11-06 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_restaurant_current_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='note',
            field=models.CharField(default='', max_length=300),
        ),
    ]
