# Generated by Django 4.1.3 on 2023-01-09 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0030_alter_key_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'default_permissions': ('add', 'change', 'delete'), 'permissions': (('view_table', 'Can view table'),)},
        ),
    ]
