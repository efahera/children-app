# Generated by Django 5.0.7 on 2024-07-18 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childrenapp', '0004_alter_child_childdob_alter_parent1_parent1email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refund',
            name='refundApprovalDate',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='refund',
            name='refundDepositOpt',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]