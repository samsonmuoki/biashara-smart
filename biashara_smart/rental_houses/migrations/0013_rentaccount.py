# Generated by Django 3.0.8 on 2020-12-10 17:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rental_houses', '0012_auto_20201006_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.UUIDField(blank=True, null=True)),
                ('updated_by', models.UUIDField(blank=True, null=True)),
                ('account_name', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('tenant_id_no', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('premises', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental_houses.Premises')),
            ],
            options={
                'unique_together': {('premises', 'tenant_id_no')},
            },
        ),
    ]