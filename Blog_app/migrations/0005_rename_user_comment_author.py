# Generated by Django 5.1.7 on 2025-03-17 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='author',
        ),
    ]
