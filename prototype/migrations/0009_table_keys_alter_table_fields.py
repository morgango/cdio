# Generated by Django 4.1.3 on 2022-11-27 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0008_tableconstraint_remove_table_keys_table_constraints'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='keys',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prototype.key'),
        ),
        migrations.AlterField(
            model_name='table',
            name='fields',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prototype.field'),
        ),
    ]