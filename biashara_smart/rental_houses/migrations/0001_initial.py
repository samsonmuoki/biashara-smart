# Generated by Django 3.0.8 on 2020-07-30 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0002_employee_employer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('building_type', models.CharField(choices=[('appartment', 'Appartment'), ('bungallow', 'Bungalow'), ('other', 'Other')], max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.Client')),
            ],
        ),
        migrations.CreateModel(
            name='HouseUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_number', models.CharField(max_length=50)),
                ('house_type', models.CharField(choices=[('cube', 'Cube'), ('bedsitter', 'Bedsitter'), ('one_bedroom', 'One Bedroom'), ('two_bedroom', 'Two Bedroom'), ('three_bedroom', 'Three Bedroom'), ('four_bedroom', 'Four Bedroom'), ('five_bedroom', 'Five Bedroom')], max_length=50)),
                ('rent', models.DecimalField(decimal_places=2, max_digits=19)),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='rental_houses.Building')),
            ],
        ),
    ]
