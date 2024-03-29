# Generated by Django 2.2.28 on 2024-03-18 18:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tenrr', '0007_userprofile_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='buyer_note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchase_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
