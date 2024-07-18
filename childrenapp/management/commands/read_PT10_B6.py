# childrenapp/management/commands/read_PT10_B6.py

# read_PT10_B6.py is to read PT10_B6 CSV file.

# To run this command:
# python manage.py read_PT10_B6 --csv_file=C:\Users\user\Desktop\myproject\testing\testdata\PT10_B6_modified.csv 

from django.core.management.base import BaseCommand
from childrenapp.models import Child, Siblings, Health, School, PrimaryFees, SecondaryFees, Refund, Parent1, Parent2, Parent3, MotherAdd, FatherAdd, Address, Emergency, Temporary
from django.db import connection
from datetime import datetime
import csv

class Command(BaseCommand):
    help = 'Read PT10_B6_modified.csv file'

    def add_arguments(self, parser):
        parser.add_argument('--csv_file', type=str)

    def handle(self, *args, **kwargs):
        # Child.objects.all().delete()
        # Siblings.objects.all().delete()
        # Health.objects.all().delete()
        # School.objects.all().delete()
        # PrimaryFees.objects.all().delete()
        # SecondaryFees.objects.all().delete()
        # Refund.objects.all().delete()
        # Parent1.objects.all().delete()
        # Parent2.objects.all().delete()
        # Parent3.objects.all().delete()
        # MotherAdd.objects.all().delete()
        # FatherAdd.objects.all().delete()
        # Address.objects.all().delete()
        # Emergency.objects.all().delete()
        # Temporary.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE childrenapp_child_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE childrenapp_siblings_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE childrenapp_Health_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE childrenapp_School_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE childrenapp_PrimaryFees_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE childrenapp_SecondaryFees_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE childrenapp_Refund_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE childrenapp_Parent1_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE childrenapp_Parent2_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE childrenapp_Parent3_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE childrenapp_MotherAdd_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE childrenapp_FatherAdd_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE childrenapp_Address_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE childrenapp_Emergency_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE childrenapp_Temporary_id_seq RESTART WITH 1")

        if kwargs['csv_file']:
            self.read_PT10_B6(kwargs['csv_file'])

        self.stdout.write(self.style.SUCCESS('PT10_B6_modified.csv has been successfully updated in the database.'))        

    def read_PT10_B6(self, csv_file_path):
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:

                child, created = Child.objects.get_or_create(
                    childNo=row['childNo'],
                    defaults={
                        'childName': row['childName'],
                        'childForeignName': row['childForeignName'],
                        'childBirthID': row['childBirthID'],
                        'childGender': row['childGender'],
                        'childDOB': row['childDOB'],
                        'childAge': row['childAge'],
                        'childRace': row['childRace'],
                        'childCitizenship': row['childCitizenship'],
                        'childResidentialStatus': row['childResidentialStatus'],
                        'childReligion': row['childReligion'],
                        'childMTLanguage': row['childMTLanguage'],
                        'childToStaff': row['childToStaff'],
                        'childHouseholdIncome': row['childHouseholdIncome'],
                        'childSubsidyType': row['childSubsidyType'],
                        'childResidentialRemarks': row['childResidentialRemarks'],

                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'Child Table for child ID {child.id} updated.'))
  
                siblings, created = Siblings.objects.update_or_create(

                    child=child,
                    defaults={
                        'siblings1': row['siblings1'],
                        'siblingsRelationship1': row['siblingsRelationship1'],
                        'siblings2': row['siblings2'],
                        'siblingsRelationship2': row['siblingsRelationship2'],
                        'siblings3': row['siblings3'],
                        'siblingsRelationship3': row['siblingsRelationship3'],
                        'siblings4': row['siblings4'],
                        'siblingsRelationship4': row['siblingsRelationship4'],
                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'Siblings Table for child ID {child.id} updated.'))

                health, created = Health.objects.update_or_create(
                    child=child,
                    defaults={
                        'healthMedCon': row['healthMedCon'],
                        'healthVaccination': row['healthVaccination'],
                        'healthAllergy': row['healthAllergy'],
                        'healthSpecialDiet': row['healthSpecialDiet'],
                        'healthSpecialNeeds': row['healthSpecialNeeds'],
                        'healthFamDrNo': row['healthFamDrNo'],
                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'Health Table for child ID {child.id} updated.'))

                school, created = School.objects.update_or_create(
                    child=child,
                    defaults={
                        'schoolAdmissionDate': row['schoolAdmissionDate'],
                        'schoolWithdrawalDate': row['schoolWithdrawalDate'],
                        'schoolProgramType': row['schoolProgramType'],
                        'schoolClassname': row['schoolClassname'],
                        'schoolClassSession': row['schoolClassSession'],
                        'schoolClassLevel': row['schoolClassLevel'],
                        'schoolTransportationNo': row['schoolTransportationNo'],
                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'School Table for child ID {child.id} updated.'))

                primaryFees, created = PrimaryFees.objects.update_or_create(
                    child=child,
                    defaults={
                        'prieesPaymentMethod': row['prieesPaymentMethod'],
                        'prifeesBankName': row['prifeesBankName'],
                        'prifeesBankAccHolder': row['prifeesBankAccHolder'],
                        'prifeesBankAccCode': row['prifeesBankAccCode'],
                        'prifeesBranchCode': row['prifeesBranchCode'],
                        'prifeesBankAccNumber': row['prifeesBankAccNumber'],
                        'prifeesApprovalDate': row['prifeesApprovalDate'],
                        'prifeesAttentionTo': row['prifeesAttentionTo'],
                        'prifeesPayeeID': row['prifeesPayeeID'],
                        'prifeesAmount': row['prifeesAmount'],
                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'PrimaryFees Table for child ID {child.id} updated.'))

                secondaryFees, created = SecondaryFees.objects.update_or_create(
                    child=child,
                    defaults={
                        'secfeesPaymentMethod': row['secfeesPaymentMethod'],
                        'secfeesBankName': row['secfeesBankName'],
                        'secfeesBankAccHolder': row['secfeesBankAccHolder'],
                        'secfeesBankAccCode': row['secfeesBankAccCode'],
                        'secfeesBranchCode': row['secfeesBranchCode'],
                        'secfeesBankAccNo': row['secfeesBankAccNo'],
                        'secfeesPayeeID': row['secfeesPayeeID'],
                        'secfeesApprovalDate': row['secfeesApprovalDate'],
                        'secfeesAttentionTo': row['secfeesAttentionTo'],
                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'SecondaryFees Table for child ID {child.id} updated.'))

                refund, created = Refund.objects.update_or_create(
                    child=child,
                    defaults={
                        'refundPaymentMethod': row['refundPaymentMethod'],
                        'refundBankName': row['refundBankName'],
                        'refundBankAccHolder': row['refundBankAccHolder'],
                        'refundBankAccCode': row['refundBankAccCode'],
                        'refundBranchCode': row['refundBranchCode'],
                        'refundBankAccNo': row['refundBankAccNo'],
                        'refundApprovalReference': row['refundApprovalReference'],
                        'refundApprovalDate': row['refundApprovalDate'],
                        'refundDepositOpt': row['refundDepositOpt'],
                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'Refund Table for child ID {child.id} updated.'))

                parent1, created = Parent1.objects.update_or_create(
                    child=child,
                    defaults={
                        'parent1Relationship': row['parent1Relationship'],
                        'parent1Name': row['parent1Name'],
                        'parent1Email': row['parent1Email'],
                        'parent1Mobile': row['parent1Mobile'],
                        'parent1Phone': row['parent1Phone'],
                        'parent1ID': row['parent1ID'],
                        'parent1Race': row['parent1Race'],
                        'parent1Citizenship': row['parent1Citizenship'],
                        'parent1Occupation': row['parent1Occupation'],
                        'parent1MainContact': row['parent1MainContact'],
                        'parent1AuthorisedPickUp': row['parent1AuthorisedPickUp'],
                        'parent1EmailInvoiceReceipt': row['parent1EmailInvoiceReceipt'],
                        'parent1EmailCheckIn': row['parent1EmailCheckIn'],
                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'Parent1 Table for child ID {child.id} updated.'))

                parent2, created = Parent2.objects.update_or_create(
                    child=child,
                    defaults={
                        'parent2Relationship': row['parent2Relationship'],
                        'parent2Name': row['parent2Name'],
                        'parent2Email': row['parent2Email'],
                        'parent2Mobile': row['parent2Mobile'],
                        'parent2Phone': row['parent2Phone'],
                        'parent2ID': row['parent2ID'],
                        'parent2Race': row['parent2Race'],
                        'parent2Citizenship': row['parent2Citizenship'],
                        'parent2Occupation': row['parent2Occupation'],
                        'parent2MainContact': row['parent2MainContact'],
                        'parent2AuthorisedPickUp': row['parent2AuthorisedPickUp'],
                        'parent2EmailInvoiceReceipt': row['parent2EmailInvoiceReceipt'],
                        'parent2EmailCheckIn': row['parent2EmailCheckIn'],
                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'Parent2 Table for child ID {child.id} updated.'))

                parent3, created = Parent3.objects.update_or_create(
                    child=child,
                    defaults={
                        'parent3Relationship': row['parent3Relationship'],
                        'parent3Name': row['parent3Name'],
                        'parent3Email': row['parent3Email'],
                        'parent3Mobile': row['parent3Mobile'],
                        'parent3Phone': row['parent3Phone'],
                        'parent3ID': row['parent3ID'],
                        'parent3Race': row['parent3Race'],
                        'parent3Citizenship': row['parent3Citizenship'],
                        'parent3Occupation': row['parent3Occupation'],
                        'parent3MainContact': row['parent3MainContact'],
                        'parent3AuthorisedPickUp': row['parent3AuthorisedPickUp'],
                        'parent3EmailInvoiceReceipt': row['parent3EmailInvoiceReceipt'],
                        'parent3EmailCheckIn': row['parent3EmailCheckIn'],
                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'Parent3 Table for child ID {child.id} updated.'))

                motherAdd, created = MotherAdd.objects.update_or_create(
                    child=child,
                    defaults={
                        'motherAddBlock': row['motherAddBlock'],
                        'motherAddBuilding': row['motherAddBuilding'],
                        'motherAddStreet': row['motherAddStreet'],
                        'motherAddUnit': row['motherAddUnit'],
                        'motherAddPostalCode': row['motherAddPostalCode'],
                        'motherAddTransport': row['motherAddTransport'],
                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'MotherAdd Table for child ID {child.id} updated.'))

                fatherAdd, created = FatherAdd.objects.update_or_create(
                    child=child,
                    defaults={
                        'fatherAddBlock': row['fatherAddBlock'],
                        'fatherAddBuilding': row['fatherAddBuilding'],
                        'fatherAddStreet': row['fatherAddStreet'],
                        'fatherAddUnit': row['fatherAddUnit'],
                        'fatherAddPostalCode': row['fatherAddPostalCode'],
                        'fatherAddTransport': row['fatherAddTransport'],
                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'FatherAdd Table for child ID {child.id} updated.'))

                address, created = Address.objects.update_or_create(
                    child=child,
                    defaults={
                        'address1Line1': row['address1Line1'],
                        'address1Line2': row['address1Line2'],
                        'address1PostalCode': row['address1PostalCode'],
                        'address1Transport': row['address1Transport'],
                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'Address Table for child ID {child.id} updated.'))

                emergency, created = Emergency.objects.update_or_create(
                    child=child,
                    defaults={
                        'emergency1Relationship': row['emergency1Relationship'],
                        'emergency1Name': row['emergency1Name'],
                        'emergency1Mobile': row['emergency1Mobile'],
                        'emergency1Phone': row['emergency1Phone'],
                        'emergency1Email': row['emergency1Email'],
                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'Emergency Table for child ID {child.id} updated.'))

                # temporary, created = Temporary.objects.update_or_create(
                #     child=child,
                #     defaults={
                #     }
                # )
                # self.stdout.write(self.style.SUCCESS(f'Temporary Table for child ID {child.id} updated.'))
