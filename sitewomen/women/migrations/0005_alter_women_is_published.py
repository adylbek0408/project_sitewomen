# Generated by Django 4.2.9 on 2024-01-19 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0004_alter_women_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=1),
        ),
    ]
