# Generated by Django 5.0.7 on 2024-07-18 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childrenapp', '0003_siblings_siblings1_siblings_siblings2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='childDOB',
            field=models.CharField(blank=True),
        ),
        migrations.AlterField(
            model_name='parent1',
            name='parent1Email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='parent2',
            name='parent2Email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='parent3',
            name='parent3Email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='primaryfees',
            name='prifeesAmount',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='primaryfees',
            name='prifeesApprovalDate',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='refund',
            name='refundApprovalDate',
            field=models.CharField(blank=True),
        ),
        migrations.AlterField(
            model_name='secondaryfees',
            name='secfeesApprovalDate',
            field=models.CharField(blank=True),
        ),
    ]