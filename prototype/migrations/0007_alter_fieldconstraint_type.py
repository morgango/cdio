# Generated by Django 4.1.3 on 2022-11-27 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0006_rename_constraint_fieldconstraint_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldconstraint',
            name='type',
            field=models.CharField(choices=[('String', 'string'), ('Numeric', 'numeric'), ('Collection', 'collection'), ('Temporal', 'temporal'), ('Any', 'any')], max_length=20),
        ),
    ]
