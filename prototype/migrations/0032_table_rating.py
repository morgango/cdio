# Generated by Django 4.1.3 on 2023-01-16 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0031_alter_table_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(0, '☆☆☆☆☆'), (1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], default=0),
        ),
    ]
