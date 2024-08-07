# childrenapp/management/commands/read_update_program.py 

# read_update_program.py is to read PT10_B6 CSV file, update Temporary table and update CoreServiceFamily table.

# To run this command:
# python manage.py read_update_program --csv_file=C:\Users\user\Desktop\myproject\testing\testdata\PT10_B6_modified.csv 

from django.core.management.base import BaseCommand
from childrenapp.models import Child, Siblings, Health, School, PrimaryFees, SecondaryFees, Refund, Parent1, Parent2, Parent3, MotherAdd, FatherAdd, Address, Emergency, Temporary, CoreServiceFamily
from django.db import connection
import csv

class Command(BaseCommand):
    help = 'Read PT10_B6_modified.csv file, update Temporary table, update CoreServiceFamily from Temporary' 

    def add_arguments(self, parser):
        parser.add_argument('--csv_file', type=str)

    def handle(self, *args, **kwargs):
        CoreServiceFamily.objects.all().delete() 

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

            cursor.execute("ALTER SEQUENCE childrenapp_coreservicefamily_id_seq RESTART WITH 1") 

        if kwargs['csv_file']:
            self.read_PT10_B6(kwargs['csv_file'])

        self.update_temporary()
        self.update_CSF_records() 

        self.stdout.write(self.style.SUCCESS('Successfully updated CoreServiceFamily records.')) 

# Read CSV file
    def read_PT10_B6(self, csv_file_path):
        count = 0
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
                count += 1

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
            
            self.stdout.write(self.style.SUCCESS(f'Successfully read {count} child records and has been added into database.'))

# Update Temporary Table
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
        
        self.stdout.write(self.style.SUCCESS('Successfully updated Temporary Table records.'))

# Update CoreServiceFamily Table
    def update_CSF_records(self):
        temporary_records = Temporary.objects.all()
        for temp in temporary_records:
            
            if temp.tempParent1 is not None:
                address = self.get_relationship(temp.temp_parent1Relationship, temp.tempMotherAdd, temp.tempFatherAdd)
                CoreServiceFamily.objects.create(
                    CSFTemporary=temp,
                    CSFChild=temp.tempChild,
                    firstName=self.get_first_name(temp.temp_parent1Name),
                    lastName=self.get_last_name(temp.temp_parent1Name),
                    phone=self.get_contact_parent1(temp.temp_parent1Mobile, temp.temp_parent1Phone),
                    email=temp.temp_parent1Email,
                    birthIC=temp.temp_parent1ID,
                    birthCountry=self.get_birthCode(temp.temp_parent1Citizenship), 
                    occupation=temp.temp_parent1Occupation,
                    relationship=temp.temp_parent1Relationship,
                    isAllowPickup=temp.temp_parent1MainContact,
                    isBillable=temp.temp_parent1AuthorisedPickUp,
                    isPrimary=temp.temp_parent1EmailInvoiceReceipt,
                    address=address,
                    postcode=self.get_postcode(temp.temp_parent1Relationship, temp.tempMotherAdd, temp.tempFatherAdd),
                )

            if temp.tempParent2 is not None:
                address = self.get_relationship(temp.temp_parent2Relationship, temp.tempMotherAdd, temp.tempFatherAdd)
                CoreServiceFamily.objects.create(
                    CSFTemporary=temp,
                    CSFChild=temp.tempChild,
                    firstName=self.get_first_name(temp.temp_parent2Name),
                    lastName=self.get_last_name(temp.temp_parent2Name),
                    phone=self.get_contact_parent2(temp.temp_parent2Mobile, temp.temp_parent2Phone),
                    email=temp.temp_parent2Email,
                    birthIC=temp.temp_parent2ID,
                    birthCountry=self.get_birthCode(temp.temp_parent2Citizenship),  
                    occupation=temp.temp_parent2Occupation,
                    relationship=temp.temp_parent2Relationship,
                    isAllowPickup=temp.temp_parent2MainContact,
                    isBillable=temp.temp_parent2AuthorisedPickUp,
                    isPrimary=temp.temp_parent2EmailInvoiceReceipt,
                    address=address,
                    postcode=self.get_postcode(temp.temp_parent2Relationship, temp.tempMotherAdd, temp.tempFatherAdd),
                )

            if temp.tempParent3 is not None and temp.temp_parent3Name != '':
                CoreServiceFamily.objects.create(
                    CSFTemporary=temp,
                    CSFChild=temp.tempChild,
                    firstName=self.get_first_name(temp.temp_parent3Name),
                    lastName=self.get_last_name(temp.temp_parent3Name),
                    phone=self.get_contact_parent3(temp.temp_parent3Mobile, temp.temp_parent3Phone),
                    email=temp.temp_parent3Email,
                    birthIC=temp.temp_parent3ID,
                    birthCountry=self.get_birthCode(temp.temp_parent3Citizenship),  
                    occupation=temp.temp_parent3Occupation,
                    relationship=temp.temp_parent3Relationship,
                    isAllowPickup=temp.temp_parent3MainContact,
                    isBillable=temp.temp_parent3AuthorisedPickUp,
                    isPrimary=temp.temp_parent3EmailInvoiceReceipt,
                    address=self.get_address_line(temp.temp_address1Line1, temp.temp_address1Line2), #added line
                    postcode=temp.temp_address1PostalCode, #added line
                )   

    def get_first_name(self, full_name):
        names = full_name.split()
        if len(names) == 1:
            return names[0]
        elif len(names) == 2:
            return names[0]
        elif len(names) == 3:
            return ' '.join(names[1:])
        elif len(names) == 4:
            return ' '.join(names[2:])
        return ''

    def get_last_name(self, full_name):
        names = full_name.split()
        if len(names) == 2:
            return names[1]
        elif len(names) == 3:
            return names[0]
        elif len(names) == 4:
            return names[1]
        return ''

    def get_contact_parent1(self, mobile, phone):
        if mobile:
            if mobile[3] != '-':
                if mobile[0] == '1':
                    return '+60' + mobile
                elif mobile[0] == '0':
                    return '+6' + mobile
                return mobile

            elif mobile[3] == '-':
                mobile = mobile[:3] + mobile[4:]  
                if mobile[0] == '1':
                    return '+60' + mobile
                elif mobile[0] == '0':
                    return '+6' + mobile
                return mobile

        elif phone:
            if phone[3] != '-':
                if phone[0] == '1':
                    return '+60' + phone
                elif phone[0] == '0':
                    return '+6' + phone
                return phone

            elif phone[3] == '-':
                phone = phone[:3] + phone[4:]  
                if phone[0] == '1':
                    return '+60' + phone
                elif phone[0] == '0':
                    return '+6' + phone
                return phone
        return ''

    def get_contact_parent2(self, mobile, phone):
        if mobile:
            if mobile[3] != '-':
                if mobile[0] == '1':
                    return '+60' + mobile
                elif mobile[0] == '0':
                    return '+6' + mobile
                return mobile

            elif mobile[3] == '-':
                mobile = mobile[:3] + mobile[4:]  
                if mobile[0] == '1':
                    return '+60' + mobile
                elif mobile[0] == '0':
                    return '+6' + mobile
                return mobile

        elif phone:
            if phone[3] != '-':
                if phone[0] == '1':
                    return '+60' + phone
                elif phone[0] == '0':
                    return '+6' + phone
                return phone

            elif phone[3] == '-':
                phone = phone[:3] + phone[4:]  
                if phone[0] == '1':
                    return '+60' + phone
                elif phone[0] == '0':
                    return '+6' + phone
                return phone
        return ''

    def get_contact_parent3(self, mobile, phone):
        if mobile:
            if mobile[3] != '-':
                if mobile[0] == '1':
                    return '+60' + mobile
                elif mobile[0] == '0':
                    return '+6' + mobile
                return mobile

            elif mobile[3] == '-':
                mobile = mobile[:3] + mobile[4:]  
                if mobile[0] == '1':
                    return '+60' + mobile
                elif mobile[0] == '0':
                    return '+6' + mobile
                return mobile

        elif phone:
            if phone[3] != '-':
                if phone[0] == '1':
                    return '+60' + phone
                elif phone[0] == '0':
                    return '+6' + phone
                return phone
                
            elif phone[3] == '-':
                phone = phone[:3] + phone[4:]  
                if phone[0] == '1':
                    return '+60' + phone
                elif phone[0] == '0':
                    return '+6' + phone
                return phone
        return ''

    def get_relationship(self, relationship, mother_address, father_address):
        if relationship.lower() == 'mother':
            return self.mother_full_add(mother_address)
        elif relationship.lower() == 'father':
            return self.father_full_add(father_address)
        else:
            return '' 

    def get_postcode(self, relationship, mother_address, father_address):
        if relationship == 'mother':
            return mother_address.motherAddPostalCode if mother_address else ''
        elif relationship == 'father':
            return father_address.fatherAddPostalCode if father_address else ''
        else:
            return ''

    def mother_full_add(self, address):
        if address:
            return ' '.join(filter(None, [
                address.motherAddUnit if hasattr(address, 'motherAddUnit') else '',
                address.motherAddStreet if hasattr(address, 'motherAddStreet') else '',
                address.motherAddBuilding if hasattr(address, 'motherAddBuilding') else '',
                address.motherAddBlock if hasattr(address, 'motherAddBlock') else '',
            ]))
        return ''

    def father_full_add(self, address):
        if address:
            return ' '.join(filter(None, [
                address.fatherAddUnit if hasattr(address, 'fatherAddUnit') else '',
                address.fatherAddStreet if hasattr(address, 'fatherAddStreet') else '',
                address.fatherAddBuilding if hasattr(address, 'fatherAddBuilding') else '',
                address.fatherAddBlock if hasattr(address, 'fatherAddBlock') else '',
            ]))
        return ''

    def get_birthCode(self, birthCountry):
        if birthCountry.lower() == 'malaysian' or birthCountry.lower() == 'malaysia':
            return 'MY'
        return birthCountry

    def get_address_line(self, address1Line1, address1Line2):
        combined_address = []
        if address1Line1:
            combined_address.append(address1Line1)
        if address1Line2:
            combined_address.append(address1Line2)
        return ' '.join(combined_address)
