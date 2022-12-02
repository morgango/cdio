# Generated by Django 4.1.3 on 2022-12-02 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0019_remove_key_foreign_table_alter_field_constraints_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='fields',
        ),
        migrations.AddField(
            model_name='table',
            name='fields',
            field=models.ManyToManyField(blank=True, null=True, to='prototype.field'),
        ),
    ]
