# Generated by Django 5.0.7 on 2024-08-27 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('childrenapp', '0010_remove_primaryfees_prieespaymentmethod_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temporary',
            old_name='temp_prieesPaymentMethod',
            new_name='temp_prifeesPaymentMethod',
        ),
    ]
