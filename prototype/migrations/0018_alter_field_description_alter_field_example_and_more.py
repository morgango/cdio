# Generated by Django 4.1.3 on 2022-11-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0017_alter_field_subtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='example',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='format',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='fieldconstraint',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='key',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='key',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tableconstraint',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tableconstraint',
            name='type',
            field=models.CharField(choices=[('Expression', 'expression'), ('Any', 'any')], max_length=20, null=True),
        ),
    ]
