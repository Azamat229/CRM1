# Generated by Django 3.1 on 2020-09-07 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_check_mealsid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='servicefee',
            field=models.ForeignKey(default=33, on_delete=django.db.models.deletion.CASCADE, to='food.servicepercentage'),
        ),
    ]
