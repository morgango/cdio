# Generated by Django 4.1.3 on 2023-01-05 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prototype', '0023_remove_key_fields_key_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
