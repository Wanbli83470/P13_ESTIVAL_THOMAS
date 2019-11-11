# Generated by Django 2.2 on 2019-04-21 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ateliers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('nb_places', models.IntegerField()),
                ('places', models.BooleanField()),
                ('date', models.DateTimeField()),
                ('lieux', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Membres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('ateliers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoga_website.Ateliers')),
            ],
        ),
    ]
