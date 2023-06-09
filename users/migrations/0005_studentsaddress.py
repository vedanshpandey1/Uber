# Generated by Django 4.2 on 2023-05-25 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_orders_order_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(blank=True, max_length=19, null=True)),
                ('house_number', models.IntegerField(blank=True, max_length=5, null=True)),
                ('city', models.CharField(blank=True, max_length=18, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('pincode', models.IntegerField(blank=True, max_length=6, null=True)),
                ('students', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.students')),
            ],
        ),
    ]
