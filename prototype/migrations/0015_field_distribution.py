# Generated by Django 4.1.3 on 2022-11-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0014_field_expression_alter_key_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='distribution',
            field=models.CharField(choices=[('Normal', 'normal'), ('Uniform', 'uniform'), ('Exponential', 'exponential'), ('Binomial', 'binomial'), ('Bernoulli', 'bernoulli'), ('Poisson', 'poisson'), ('Custom', 'custom')], max_length=20, null=True),
        ),
    ]
