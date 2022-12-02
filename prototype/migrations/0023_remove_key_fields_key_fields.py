# Generated by Django 4.1.3 on 2022-12-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0022_remove_table_constraints_alter_table_fields_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='key',
            name='fields',
        ),
        migrations.AddField(
            model_name='key',
            name='fields',
            field=models.ManyToManyField(blank=True, to='prototype.field'),
        ),
    ]
