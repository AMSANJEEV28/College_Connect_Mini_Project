# Generated by Django 4.2.1 on 2023-12-17 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_alter_post_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='groups',
        ),
    ]
