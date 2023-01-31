# Generated by Django 4.1.3 on 2023-01-30 18:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prototype', '0033_remove_table_rating_rating_like_follow_comment_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Follow',
            new_name='Follower',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='follows',
            new_name='followers',
        ),
    ]
