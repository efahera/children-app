# Generated by Django 5.0.7 on 2024-07-17 03:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('childNo', models.CharField(max_length=100)),
                ('childName', models.CharField(max_length=100)),
                ('childForeignName', models.CharField(blank=True, max_length=100)),
                ('childBirthID', models.CharField(max_length=100)),
                ('childGender', models.CharField(max_length=100)),
                ('childDOB', models.DateField(blank=True)),
                ('childAge', models.CharField(blank=True, max_length=100)),
                ('childRace', models.CharField(blank=True, max_length=100)),
                ('childCitizenship', models.CharField(blank=True, max_length=100)),
                ('childResidentialStatus', models.CharField(blank=True, max_length=100)),
                ('childReligion', models.CharField(blank=True, max_length=100)),
                ('childMTLanguage', models.CharField(blank=True, max_length=100)),
                ('childToStaff', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=100)),
                ('childHouseholdIncome', models.CharField(blank=True, max_length=100)),
                ('childSubsidyType', models.CharField(blank=True, max_length=100)),
                ('childResidentialRemarks', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1Line1', models.CharField(blank=True, max_length=100)),
                ('address1Line2', models.CharField(blank=True, max_length=100)),
                ('address1PostalCode', models.CharField(blank=True, max_length=100)),
                ('address1Transport', models.CharField(blank=True, max_length=100)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='childrenapp.child')),
            ],
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emergency1Relationship', models.CharField(blank=True, max_length=100)),
                ('emergency1Name', models.CharField(blank=True, max_length=100)),
                ('emergency1Mobile', models.CharField(blank=True, max_length=100)),
                ('emergency1Phone', models.CharField(blank=True, max_length=100)),
                ('emergency1Email', models.CharField(blank=True, max_length=100)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='childrenapp.child')),
            ],
        ),
        migrations.CreateModel(
            name='FatherAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fatherAddBlock', models.CharField(blank=True, max_length=100)),
                ('fatherAddBuilding', models.CharField(blank=True, max_length=100)),
                ('fatherAddStreet', models.CharField(blank=True, max_length=100)),
                ('fatherAddUnit', models.CharField(blank=True, max_length=100)),
                ('fatherAddPostalCode', models.CharField(blank=True, max_length=100)),
                ('fatherAddTransport', models.CharField(blank=True, max_length=100)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='childrenapp.child')),
            ],
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('healthMedCon', models.CharField(blank=True, max_length=100)),
                ('healthVaccination', models.CharField(blank=True, max_length=100)),
                ('healthAllergy', models.CharField(blank=True, max_length=100)),
                ('healthSpecialDiet', models.CharField(blank=True, max_length=100)),
                ('healthSpecialNeeds', models.CharField(blank=True, max_length=100)),
                ('healthFamDrNo', models.CharField(blank=True, max_length=100)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='childrenapp.child')),
            ],
        ),
        migrations.CreateModel(
            name='MotherAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motherAddBlock', models.CharField(blank=True, max_length=100)),
                ('motherAddBuilding', models.CharField(blank=True, max_length=100)),
                ('motherAddStreet', models.CharField(blank=True, max_length=100)),
                ('motherAddUnit', models.CharField(blank=True, max_length=100)),
                ('motherAddPostalCode', models.CharField(blank=True, max_length=100)),
                ('motherAddTransport', models.CharField(blank=True, max_length=100)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='childrenapp.child')),
            ],
        ),
        migrations.CreateModel(
            name='Parent1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent1Relationship', models.CharField(blank=True, max_length=100)),
                ('parent1Name', models.CharField(blank=True, max_length=100)),
                ('parent1Email', models.EmailField(blank=True, max_length=100)),
                ('parent1Mobile', models.CharField(blank=True, max_length=100)),
                ('parent1Phone', models.CharField(blank=True, max_length=100)),
                ('parent1ID', models.CharField(blank=True, max_length=100)),
                ('parent1Race', models.CharField(blank=True, max_length=100)),
                ('parent1Citizenship', models.CharField(blank=True, max_length=100)),
                ('parent1Occupation', models.CharField(blank=True, max_length=100)),
                ('parent1MainContact', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=100)),
                ('parent1AuthorisedPickUp', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=100)),
                ('parent1EmailInvoiceReceipt', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=100)),
                ('parent1EmailCheckIn', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=100)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='childrenapp.child')),
            ],
        ),
        migrations.CreateModel(
            name='Parent2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent2Relationship', models.CharField(blank=True, max_length=100)),
                ('parent2Name', models.CharField(blank=True, max_length=100)),
                ('parent2Email', models.EmailField(blank=True, max_length=100)),
                ('parent2Mobile', models.CharField(blank=True, max_length=100)),
                ('parent2Phone', models.CharField(blank=True, max_length=100)),
                ('parent2ID', models.CharField(blank=True, max_length=100)),
                ('parent2Race', models.CharField(blank=True, max_length=100)),
                ('parent2Citizenship', models.CharField(blank=True, max_length=100)),
                ('parent2Occupation', models.CharField(blank=True, max_length=100)),
                ('parent2MainContact', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=100)),
                ('parent2AuthorisedPickUp', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=100)),
                ('parent2EmailInvoiceReceipt', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=100)),
                ('parent2EmailCheckIn', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=100)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='childrenapp.child')),
            ],
        ),
        migrations.CreateModel(
            name='Parent3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent3Relationship', models.CharField(blank=True, max_length=100)),
                ('parent3Name', models.CharField(blank=True, max_length=100)),
                ('parent3Email', models.EmailField(blank=True, max_length=100)),
                ('parent3Mobile', models.CharField(blank=True, max_length=100)),
                ('parent3Phone', models.CharField(blank=True, max_length=100)),
                ('parent3ID', models.CharField(blank=True, max_length=100)),
                ('parent3Race', models.CharField(blank=True, max_length=100)),
                ('parent3Citizenship', models.CharField(blank=True, max_length=100)),
                ('parent3Occupation', models.CharField(blank=True, max_length=100)),
                ('parent3MainContact', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=100)),
                ('parent3AuthorisedPickUp', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=100)),
                ('parent3EmailInvoiceReceipt', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=100)),
                ('parent3EmailCheckIn', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=100)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='childrenapp.child')),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prieesPaymentMethod', models.CharField(blank=True, max_length=100)),
                ('prifeesBankName', models.CharField(blank=True, max_length=100)),
                ('prifeesBankAccHolder', models.CharField(blank=True, max_length=100)),
                ('prifeesBankAccCode', models.CharField(blank=True, max_length=100)),
                ('prifeesBranchCode', models.CharField(blank=True, max_length=100)),
                ('prifeesBankAccNumber', models.CharField(blank=True, max_length=100)),
                ('prifeesApprovalDate', models.DateField(blank=True)),
                ('prifeesAttentionTo', models.CharField(blank=True, max_length=100)),
                ('prifeesPayeeID', models.CharField(blank=True, max_length=100)),
                ('prifeesAmount', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='childrenapp.child')),
            ],
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refundPaymentMethod', models.CharField(blank=True, max_length=100)),
                ('refundBankName', models.CharField(blank=True, max_length=100)),
                ('refundBankAccHolder', models.CharField(blank=True, max_length=100)),
                ('refundBankAccCode', models.CharField(blank=True, max_length=100)),
                ('refundBranchCode', models.CharField(blank=True, max_length=100)),
                ('refundBankAccNo', models.CharField(blank=True, max_length=100)),
                ('refundApprovalReference', models.CharField(blank=True, max_length=100)),
                ('refundApprovalDate', models.DateField(blank=True)),
                ('refundDepositOpt', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='childrenapp.child')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolAdmissionDate', models.CharField(blank=True, max_length=100)),
                ('schoolWithdrawalDate', models.CharField(blank=True, max_length=100)),
                ('schoolProgramType', models.CharField(blank=True, max_length=100)),
                ('schoolClassname', models.CharField(blank=True, max_length=100)),
                ('schoolClassSession', models.CharField(blank=True, max_length=100)),
                ('schoolClassLevel', models.CharField(blank=True, max_length=100)),
                ('schoolTransportationNo', models.CharField(blank=True, max_length=100)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='childrenapp.child')),
            ],
        ),
        migrations.CreateModel(
            name='SecondaryFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secfeesPaymentMethod', models.CharField(blank=True, max_length=100)),
                ('secfeesBankName', models.CharField(blank=True, max_length=100)),
                ('secfeesBankAccHolder', models.CharField(blank=True, max_length=100)),
                ('secfeesBankAccCode', models.CharField(blank=True, max_length=100)),
                ('secfeesBranchCode', models.CharField(blank=True, max_length=100)),
                ('secfeesBankAccNo', models.CharField(blank=True, max_length=100)),
                ('secfeesApprovalDate', models.DateField(blank=True)),
                ('secfeesAttentionTo', models.CharField(blank=True, max_length=100)),
                ('secfeesPayeeID', models.CharField(blank=True, max_length=100)),
                ('secfeesAmount', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='childrenapp.child')),
            ],
        ),
        migrations.CreateModel(
            name='Siblings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siblings1', models.CharField(blank=True, max_length=100)),
                ('siblingsRelationship1', models.CharField(blank=True, max_length=100)),
                ('siblings2', models.CharField(blank=True, max_length=100)),
                ('siblingsRelationship2', models.CharField(blank=True, max_length=100)),
                ('siblings3', models.CharField(blank=True, max_length=100)),
                ('siblingsRelationship3', models.CharField(blank=True, max_length=100)),
                ('siblings4', models.CharField(blank=True, max_length=100)),
                ('siblingsRelationship4', models.CharField(blank=True, max_length=100)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='childrenapp.child')),
            ],
        ),
        migrations.CreateModel(
            name='Temporary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tempAddress', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='childrenapp.address')),
                ('tempChild', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='childrenapp.child')),
                ('tempEmergency', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='childrenapp.emergency')),
                ('tempFatherAdd', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='childrenapp.fatheradd')),
                ('tempHealth', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='childrenapp.health')),
                ('tempMotherAdd', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='childrenapp.motheradd')),
                ('tempParent1', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='childrenapp.parent1')),
                ('tempParent2', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='childrenapp.parent2')),
                ('tempParent3', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='childrenapp.parent3')),
                ('tempPrimaryFees', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='childrenapp.primaryfees')),
                ('tempRefund', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='childrenapp.refund')),
                ('tempSchool', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='childrenapp.school')),
                ('tempSecondaryFees', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='childrenapp.secondaryfees')),
                ('tempSiblings', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='childrenapp.siblings')),
            ],
        ),
    ]
