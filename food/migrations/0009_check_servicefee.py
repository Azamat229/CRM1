# Generated by Django 3.1 on 2020-09-06 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_remove_check_servicefee'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='servicefee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='food.servicepercentage'),
            preserve_default=False,
        ),
    ]
