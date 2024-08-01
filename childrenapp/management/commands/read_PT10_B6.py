# childrenapp/management/commands/read_PT10_B6.py

# read_PT10_B6.py is to read PT10_B6 CSV file.

# To run this command:
# python manage.py read_PT10_B6 --csv_file=C:\Users\user\Desktop\myproject\testing\testdata\PT10_B6_modified.csv 

from django.core.management.base import BaseCommand
from childrenapp.models import Child, Siblings, Health, School, PrimaryFees, SecondaryFees, Refund, Parent1, Parent2, Parent3, MotherAdd, FatherAdd, Address, Emergency, Temporary, CoreServiceFamily
from django.db import connection
import csv

class Command(BaseCommand):
    help = 'Read PT10_B6_modified.csv file and update Temporary table'

    def add_arguments(self, parser):
        parser.add_argument('--csv_file', type=str)

    def handle(self, *args, **kwargs):

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

        self.update_temporary()

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

                address, created = Address.objects.update_or_create(
                    child=child,
                    defaults={
                        'address1Line1': row['address1Line1'],
                        'address1Line2': row['address1Line2'],
                        'address1PostalCode': row['address1PostalCode'],
                        'address1Transport': row['address1Transport'],
                    }
                ) 

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

            self.stdout.write(self.style.SUCCESS(f'Total of {child.id} records has been successfully updated.'))

    def update_temporary(self):
        Temporary.objects.all().delete()  
        
        children = Child.objects.all()
        for child in children:
            siblings = Siblings.objects.filter(child=child).first()
            health = Health.objects.filter(child=child).first()
            school = School.objects.filter(child=child).first()
            primary_fees = PrimaryFees.objects.filter(child=child).first()
            secondary_fees = SecondaryFees.objects.filter(child=child).first()
            refund = Refund.objects.filter(child=child).first()
            parent1 = Parent1.objects.filter(child=child).first()
            parent2 = Parent2.objects.filter(child=child).first()
            parent3 = Parent3.objects.filter(child=child).first()
            mother_add = MotherAdd.objects.filter(child=child).first()
            father_add = FatherAdd.objects.filter(child=child).first()
            address = Address.objects.filter(child=child).first()
            emergency = Emergency.objects.filter(child=child).first()

            Temporary.objects.create(

            # Child
                tempChild_id=child.id,
                temp_childNo=child.childNo,
                temp_childName=child.childName,
                temp_childForeignName=child.childForeignName,
                temp_childBirthID=child.childBirthID,
                temp_childGender=child.childGender,
                temp_childDOB=child.childDOB,
                temp_childAge=child.childAge,
                temp_childRace=child.childRace,
                temp_childCitizenship=child.childCitizenship,
                temp_childResidentialStatus=child.childResidentialStatus,
                temp_childReligion=child.childReligion,
                temp_childMTLanguage=child.childMTLanguage,
                temp_childToStaff=child.childToStaff,
                temp_childHouseholdIncome=child.childHouseholdIncome,
                temp_childSubsidyType=child.childSubsidyType,
                temp_childResidentialRemarks=child.childResidentialRemarks,

            # Siblings
                tempSiblings_id=siblings.id,
                temp_siblings1=siblings.siblings1 if siblings else None,
                temp_siblingsRelationship1=siblings.siblingsRelationship1 if siblings else None,
                temp_siblings2=siblings.siblings2 if siblings else None,
                temp_siblingsRelationship2=siblings.siblingsRelationship2 if siblings else None,
                temp_siblings3=siblings.siblings3 if siblings else None,
                temp_siblingsRelationship3=siblings.siblingsRelationship3 if siblings else None,
                temp_siblings4=siblings.siblings4 if siblings else None,
                temp_siblingsRelationship4=siblings.siblingsRelationship4 if siblings else None,
            
            # Health
                tempHealth_id=health.id,
                temp_healthMedCon=health.healthMedCon if health else None,
                temp_healthVaccination=health.healthVaccination if health else None,
                temp_healthAllergy=health.healthAllergy if health else None,
                temp_healthSpecialDiet=health.healthSpecialDiet if health else None,
                temp_healthSpecialNeeds=health.healthSpecialNeeds if health else None,
                temp_healthFamDrNo=health.healthFamDrNo if health else None,

            # School
                tempSchool_id=school.id,
                temp_schoolAdmissionDate=school.schoolAdmissionDate if school else None,
                temp_schoolWithdrawalDate=school.schoolWithdrawalDate if school else None,
                temp_schoolProgramType=school.schoolProgramType if school else None,
                temp_schoolClassname=school.schoolClassname if school else None,
                temp_schoolClassSession=school.schoolClassSession if school else None,
                temp_schoolClassLevel=school.schoolClassLevel if school else None,
                temp_schoolTransportationNo=school.schoolTransportationNo if school else None,

            # PrimaryFees
                tempPrimaryFees_id=primary_fees.id,
                temp_prieesPaymentMethod=primary_fees.prieesPaymentMethod if primary_fees else None,
                temp_prifeesBankName=primary_fees.prifeesBankName if primary_fees else None,
                temp_prifeesBankAccHolder=primary_fees.prifeesBankAccHolder if primary_fees else None,
                temp_prifeesBankAccCode=primary_fees.prifeesBankAccCode if primary_fees else None,
                temp_prifeesBranchCode=primary_fees.prifeesBranchCode if primary_fees else None,
                temp_prifeesBankAccNumber=primary_fees.prifeesBankAccNumber if primary_fees else None,
                temp_prifeesApprovalDate=primary_fees.prifeesApprovalDate if primary_fees else None,
                temp_prifeesAttentionTo=primary_fees.prifeesAttentionTo if primary_fees else None,
                temp_prifeesPayeeID=primary_fees.prifeesPayeeID if primary_fees else None,
                temp_prifeesAmount=primary_fees.prifeesAmount if primary_fees else None,

            # SecondaryFees
                tempSecondaryFees_id=secondary_fees.id,
                temp_secfeesPaymentMethod=secondary_fees.secfeesPaymentMethod if secondary_fees else None,
                temp_secfeesBankName=secondary_fees.secfeesBankName if secondary_fees else None,
                temp_secfeesBankAccHolder=secondary_fees.secfeesBankAccHolder if secondary_fees else None,
                temp_secfeesBankAccCode=secondary_fees.secfeesBankAccCode if secondary_fees else None,
                temp_secfeesBranchCode=secondary_fees.secfeesBranchCode if secondary_fees else None,
                temp_secfeesBankAccNo=secondary_fees.secfeesBankAccNo if secondary_fees else None,
                temp_secfeesPayeeID=secondary_fees.secfeesPayeeID if secondary_fees else None,
                temp_secfeesApprovalDate=secondary_fees.secfeesApprovalDate if secondary_fees else None,
                temp_secfeesAttentionTo=secondary_fees.secfeesAttentionTo if secondary_fees else None,

            # Refund
                tempRefund_id=refund.id,
                temp_refundPaymentMethod=refund.refundPaymentMethod if refund else None,
                temp_refundBankName=refund.refundBankName if refund else None,
                temp_refundBankAccHolder=refund.refundBankAccHolder if refund else None,
                temp_refundBankAccCode=refund.refundBankAccCode if refund else None,
                temp_refundBranchCode=refund.refundBranchCode if refund else None,
                temp_refundBankAccNo=refund.refundBankAccNo if refund else None,
                temp_refundApprovalReference=refund.refundApprovalReference if refund else None,
                temp_refundApprovalDate=refund.refundApprovalDate if refund else None,
                temp_refundDepositOpt=refund.refundDepositOpt if refund else None,

            # Parent1
                tempParent1_id=parent1.id,
                temp_parent1Relationship=parent1.parent1Relationship if parent1 else None,
                temp_parent1Name=parent1.parent1Name if parent1 else None,
                temp_parent1Email=parent1.parent1Email if parent1 else None,
                temp_parent1Mobile=parent1.parent1Mobile if parent1 else None,
                temp_parent1Phone=parent1.parent1Phone if parent1 else None,
                temp_parent1ID=parent1.parent1ID if parent1 else None,
                temp_parent1Race=parent1.parent1Race if parent1 else None,
                temp_parent1Citizenship=parent1.parent1Citizenship if parent1 else None,
                temp_parent1Occupation=parent1.parent1Occupation if parent1 else None,
                temp_parent1MainContact=parent1.parent1MainContact if parent1 else None,
                temp_parent1AuthorisedPickUp=parent1.parent1AuthorisedPickUp if parent1 else None,
                temp_parent1EmailInvoiceReceipt=parent1.parent1EmailInvoiceReceipt if parent1 else None,
                temp_parent1EmailCheckIn=parent1.parent1EmailCheckIn if parent1 else None,

            # Parent2
                tempParent2_id=parent2.id,
                temp_parent2Relationship=parent2.parent2Relationship if parent2 else None,
                temp_parent2Name=parent2.parent2Name if parent2 else None,
                temp_parent2Email=parent2.parent2Email if parent2 else None,
                temp_parent2Mobile=parent2.parent2Mobile if parent2 else None,
                temp_parent2Phone=parent2.parent2Phone if parent2 else None,
                temp_parent2ID=parent2.parent2ID if parent2 else None,
                temp_parent2Race=parent2.parent2Race if parent2 else None,
                temp_parent2Citizenship=parent2.parent2Citizenship if parent2 else None,
                temp_parent2Occupation=parent2.parent2Occupation if parent2 else None,
                temp_parent2MainContact=parent2.parent2MainContact if parent2 else None,
                temp_parent2AuthorisedPickUp=parent2.parent2AuthorisedPickUp if parent2 else None,
                temp_parent2EmailInvoiceReceipt=parent2.parent2EmailInvoiceReceipt if parent2 else None,
                temp_parent2EmailCheckIn=parent2.parent2EmailCheckIn if parent2 else None,

            # Parent3
                tempParent3_id=parent3.id,
                temp_parent3Relationship=parent3.parent3Relationship if parent3 else None,
                temp_parent3Name=parent3.parent3Name if parent3 else None,
                temp_parent3Email=parent3.parent3Email if parent3 else None,
                temp_parent3Mobile=parent3.parent3Mobile if parent3 else None,
                temp_parent3Phone=parent3.parent3Phone if parent3 else None,
                temp_parent3ID=parent3.parent3ID if parent3 else None,
                temp_parent3Race=parent3.parent3Race if parent3 else None,
                temp_parent3Citizenship=parent3.parent3Citizenship if parent3 else None,
                temp_parent3Occupation=parent3.parent3Occupation if parent3 else None,
                temp_parent3MainContact=parent3.parent3MainContact if parent3 else None,
                temp_parent3AuthorisedPickUp=parent3.parent3AuthorisedPickUp if parent3 else None,
                temp_parent3EmailInvoiceReceipt=parent3.parent3EmailInvoiceReceipt if parent3 else None,
                temp_parent3EmailCheckIn=parent3.parent3EmailCheckIn if parent3 else None,

            # MotherAdd
                tempMotherAdd_id=mother_add.id,
                temp_motherAddBlock=mother_add.motherAddBlock if mother_add else None,
                temp_motherAddBuilding=mother_add.motherAddBuilding if mother_add else None,
                temp_motherAddStreet=mother_add.motherAddStreet if mother_add else None,
                temp_motherAddUnit=mother_add.motherAddUnit if mother_add else None,
                temp_motherAddPostalCode=mother_add.motherAddPostalCode if mother_add else None,
                temp_motherAddTransport=mother_add.motherAddTransport if mother_add else None,

            # FatherAdd
                tempFatherAdd_id=father_add.id,
                temp_fatherAddBlock=father_add.fatherAddBlock if father_add else None,
                temp_fatherAddBuilding=father_add.fatherAddBuilding if father_add else None,
                temp_fatherAddStreet=father_add.fatherAddStreet if father_add else None,
                temp_fatherAddUnit=father_add.fatherAddUnit if father_add else None,
                temp_fatherAddPostalCode=father_add.fatherAddPostalCode if father_add else None,
                temp_fatherAddTransport=father_add.fatherAddTransport if father_add else None,

            # Address
                tempAddress_id=address.id,
                temp_address1Line1=address.address1Line1 if address else None,
                temp_address1Line2=address.address1Line2 if address else None,
                temp_address1PostalCode=address.address1PostalCode if address else None,
                temp_address1Transport=address.address1Transport if address else None,

            # Emergency
                tempEmergency_id=emergency.id,
                temp_emergency1Relationship=emergency.emergency1Relationship if emergency else None,
                temp_emergency1Name=emergency.emergency1Name if emergency else None,
                temp_emergency1Mobile=emergency.emergency1Mobile if emergency else None,
                temp_emergency1Phone=emergency.emergency1Phone if emergency else None,
                temp_emergency1Email=emergency.emergency1Email if emergency else None,

            )
        
        self.stdout.write(self.style.SUCCESS('Temporary Table has been successfully updated.'))