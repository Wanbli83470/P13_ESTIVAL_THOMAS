# Generated by Django 2.2 on 2019-10-30 06:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yoga_website', '0014_clients'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ateliers',
            new_name='Atelier',
        ),
        migrations.RenameModel(
            old_name='Clients',
            new_name='Client',
        ),
    ]
