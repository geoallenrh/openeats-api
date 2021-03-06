# Generated by Django 2.0.1 on 2019-03-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0015_remove_recipe_old_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='subrecipe',
            name='denominator',
            field=models.FloatField(default=1, verbose_name='denominator'),
        ),
        migrations.AddField(
            model_name='subrecipe',
            name='numerator',
            field=models.FloatField(default=0, verbose_name='numerator'),
        ),
    ]
