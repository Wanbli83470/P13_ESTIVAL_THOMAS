# Generated by Django 2.2 on 2019-04-25 17:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga_website', '0012_auto_20190425_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ateliers',
            name='participants',
            field=models.ManyToManyField(default='admin', to=settings.AUTH_USER_MODEL),
        ),
    ]
