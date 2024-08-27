# views.py

import os
import csv
from .models import Child, Siblings, Health, School, PrimaryFees, SecondaryFees, Refund, Parent1, Parent2, Parent3, MotherAdd, FatherAdd, Address, Emergency, Temporary, CoreServiceFamily, CoreServiceChildrenMedicalContact, Staff
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class UploadChildrenCSVData(APIView):

    def get(self, request, *args, **kwargs):
        return render(request, 'upload_csv.html')  

    def post(self, request, *args, **kwargs):
        CoreServiceFamily.objects.all().delete()
        CoreServiceChildrenMedicalContact.objects.all().delete()
        Staff.objects.all().delete()

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
            cursor.execute("ALTER SEQUENCE childrenapp_coreservicechildrenmedicalcontact_id_seq RESTART WITH 1") 
            cursor.execute("ALTER SEQUENCE childrenapp_Staff_id_seq RESTART WITH 1")

        csv_file = request.FILES.get('csv_file')
        staff_csv_file = request.FILES.get('staff_csv_file')

        if csv_file and staff_csv_file:
            try:            
                self.read_PT10_B6(csv_file)
                self.read_staff_list(staff_csv_file)
                self.update_temporary()
                self.update_CSF_records()
                self.update_CSCMC_records()

                return HttpResponse("Successfully updated records from both files.")

            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        elif csv_file:
            try:
                self.read_PT10_B6(csv_file)
                self.update_temporary()
                self.update_CSF_records()
                self.update_CSCMC_records()

                return HttpResponse("Successfully updated records from children CSV file.")
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        elif staff_csv_file:
            try:
                self.read_staff_list(staff_csv_file)

                return HttpResponse("Successfully updated records from staff CSV file.")
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return HttpResponse("No CSV file uploaded.", status=400)

# Read CSV file
    def read_PT10_B6(self, csv_file):

        file = csv_file.read().decode('utf-8').splitlines()
        data = file[4:]
        reader = csv.DictReader(data)

        for row in reader:
            childNo = row['No']
            childName = row['Name']
            childForeignName = row['Foreign Name']
            childBirthID = row['Student ID (BC Number)']
            childGender = row['Gender']
            childDOB = row['Dob']
            childAge = row['Age']
            childRace = row['Race']
            childCitizenship = row['Citizenship']
            childResidentialStatus = row['Residential Status']
            childReligion = row['Religion']
            childMTLanguage = row['Mother Tongue language']
            childToStaff = row['Child of a staff']
            childHouseholdIncome = row['Household Income']
            childSubsidyType = row['Subsidy Type']
            childResidentialRemarks = row['Other Residential Remarks']

            child, created = Child.objects.get_or_create(
                childNo=childNo,
                defaults={
                    'childName': childName,
                    'childForeignName': childForeignName,
                    'childBirthID': childBirthID,
                    'childGender': childGender,
                    'childDOB': childDOB,
                    'childAge': childAge,
                    'childRace': childRace,
                    'childCitizenship': childCitizenship,
                    'childResidentialStatus': childResidentialStatus,
                    'childReligion': childReligion,
                    'childMTLanguage': childMTLanguage,
                    'childToStaff': childToStaff,
                    'childHouseholdIncome': childHouseholdIncome,
                    'childSubsidyType': childSubsidyType,
                    'childResidentialRemarks': childResidentialRemarks,
                }
            )             

            siblings1 = row['Siblings 1']
            siblingsRelationship1 = row['Siblings Relationship 1']
            siblings2 = row['Siblings 2']
            siblingsRelationship2 = row['Siblings Relationship 2']
            siblings3 = row['Siblings 3']
            siblingsRelationship3 = row['Siblings Relationship 3']
            siblings4 = row['Siblings 4']
            siblingsRelationship4 = row['Siblings Relationship 4']
	
            siblings, created = Siblings.objects.update_or_create(
                child=child,
                defaults={
                    'siblings1': siblings1,
                    'siblingsRelationship1': siblingsRelationship1,
                    'siblings2': siblings2,
                    'siblingsRelationship2': siblingsRelationship2,
                    'siblings3': siblings3,
                    'siblingsRelationship3': siblingsRelationship3,
                    'siblings4': siblings4,
                    'siblingsRelationship4': siblingsRelationship4,
                }
            ) 

            healthMedCon = row['Medical Conditions']
            healthVaccination = row['Vaccination History']
            healthAllergy = row['Allergy History (Food/Medication)']
            healthSpecialDiet = row['Special Diet']
            healthSpecialNeeds = row['Special Needs']
            healthFamDrNo = row['Family Doctor Number']

            health, created = Health.objects.update_or_create(
                child=child,
                defaults={
                    'healthMedCon': healthMedCon,
                    'healthVaccination': healthVaccination,
                    'healthAllergy': healthAllergy,
                    'healthSpecialDiet': healthSpecialDiet,
                    'healthSpecialNeeds': healthSpecialNeeds,
                    'healthFamDrNo': healthFamDrNo,
                }
            )                 

            schoolAdmissionDate = row['Admission Date']
            schoolWithdrawalDate = row['Withdrawal date']
            schoolProgramType = row['Program Type']
            schoolClassname = row['Class name']
            schoolClassSession = row['Class Session']
            schoolClassLevel = row['Class level']
            schoolTransportationNo = row['Transportation Number']

            school, created = School.objects.update_or_create(
                child=child,
                defaults={
                    'schoolAdmissionDate': schoolAdmissionDate,
                    'schoolWithdrawalDate': schoolWithdrawalDate,
                    'schoolProgramType': schoolProgramType,
                    'schoolClassname': schoolClassname,
                    'schoolClassSession': schoolClassSession,
                    'schoolClassLevel': schoolClassLevel,
                    'schoolTransportationNo': schoolTransportationNo,
                }
            ) 

            prifeesPaymentMethod = row['Primary Payment Method']
            prifeesBankName = row['Primary Bank Name']
            prifeesBankAccHolder = row['Primary Bank Account Holder']
            prifeesBankAccCode = row['Primary Bank Account Code']
            prifeesBranchCode = row['Primary Branch Code']
            prifeesBankAccNumber = row['Primary Bank Account Number']
            prifeesApprovalDate = row['Primary Payment Method Approval Date']
            prifeesAttentionTo = row['Primary Attention To']
            prifeesPayeeID = row['Primary Payee ID']
            prifeesAmount = row['Primary Amount']

            primaryFees, created = PrimaryFees.objects.update_or_create(
                child=child,
                defaults={
                    'prifeesPaymentMethod': prifeesPaymentMethod,
                    'prifeesBankName': prifeesBankName,
                    'prifeesBankAccHolder': prifeesBankAccHolder,
                    'prifeesBankAccCode': prifeesBankAccCode,
                    'prifeesBranchCode': prifeesBranchCode,
                    'prifeesBankAccNumber': prifeesBankAccNumber,
                    'prifeesApprovalDate': prifeesApprovalDate,
                    'prifeesAttentionTo': prifeesAttentionTo,
                    'prifeesPayeeID': prifeesPayeeID,
                    'prifeesAmount': prifeesAmount,
                }
            ) 

            secfeesPaymentMethod = row['Secondary Payment Method']
            secfeesBankName = row['Secondary Bank Name']
            secfeesBankAccHolder = row['Secondary Bank Account Holder']
            secfeesBankAccCode = row['Secondary Bank Account Code']
            secfeesBranchCode = row['Secondary Branch Code']
            secfeesBankAccNo = row['Secondary Bank Account Number']
            secfeesPayeeID = row['Secondary Payee ID']
            secfeesApprovalDate = row['Secondary Payment Method Approval Date']
            secfeesAttentionTo = row['Secondary Attention To']

            secondaryFees, created = SecondaryFees.objects.update_or_create(
                child=child,
                defaults={
                    'secfeesPaymentMethod': secfeesPaymentMethod,
                    'secfeesBankName': secfeesBankName,
                    'secfeesBankAccHolder': secfeesBankAccHolder,
                    'secfeesBankAccCode': secfeesBankAccCode,
                    'secfeesBranchCode': secfeesBranchCode,
                    'secfeesBankAccNo': secfeesBankAccNo,
                    'secfeesPayeeID': secfeesPayeeID,
                    'secfeesApprovalDate': secfeesApprovalDate,
                    'secfeesAttentionTo': secfeesAttentionTo,
                }
            ) 

            refundPaymentMethod = row['Refund Payment Method']
            refundBankName = row['Refund Bank Name']
            refundBankAccHolder = row['Refund Bank Account Holder']
            refundBankAccCode = row['Refund Bank Account Code']
            refundBranchCode = row['Refund Branch Code']
            refundBankAccNo = row['Refund Bank Account No.']
            refundApprovalReference = row['Refund Payment Method Approval Reference']
            refundApprovalDate = row['Refund Payment Method Approval Date']
            refundDepositOpt = row['Refund Deposit Option']

            refund, created = Refund.objects.update_or_create(
                child=child,
                defaults={
                    'refundPaymentMethod': refundPaymentMethod,
                    'refundBankName': refundBankName,
                    'refundBankAccHolder': refundBankAccHolder,
                    'refundBankAccCode': refundBankAccCode,
                    'refundBranchCode': refundBranchCode,
                    'refundBankAccNo': refundBankAccNo,
                    'refundApprovalReference': refundApprovalReference,
                    'refundApprovalDate': refundApprovalDate,
                    'refundDepositOpt': refundDepositOpt,
                }
            ) 

            parent1Relationship = row['Parent Relationship 1']
            parent1Name = row['Name 1']
            parent1Email = row['Email 1']
            parent1Mobile = row['Mobile No. 1']
            parent1Phone = row['Phone No. 1']
            parent1ID = row['NRIC /ID 1']
            parent1Race = row['Race 1']
            parent1Citizenship = row['Citizenship 1']
            parent1Occupation = row['Occupation 1']
            parent1MainContact = row['Main contact 1']
            parent1AuthorisedPickUp = row['Authorised Pick Up Person 1']
            parent1EmailInvoiceReceipt = row['Email Invoice Receipt 1']
            parent1EmailCheckIn = row['Email checkin 1']

            parent1, created = Parent1.objects.update_or_create(
                child=child,
                defaults={
                    'parent1Relationship': parent1Relationship,
                    'parent1Name': parent1Name,
                    'parent1Email': parent1Email,
                    'parent1Mobile': parent1Mobile,
                    'parent1Phone': parent1Phone,
                    'parent1ID': parent1ID,
                    'parent1Race': parent1Race,
                    'parent1Citizenship': parent1Citizenship,
                    'parent1Occupation': parent1Occupation,
                    'parent1MainContact': parent1MainContact,
                    'parent1AuthorisedPickUp': parent1AuthorisedPickUp,
                    'parent1EmailInvoiceReceipt': parent1EmailInvoiceReceipt,
                    'parent1EmailCheckIn': parent1EmailCheckIn,
                }
            ) 

            parent2Relationship = row['Parent Relationship 2']
            parent2Name = row['Name 2']
            parent2Email = row['Email 2']
            parent2Mobile = row['Mobile No. 2']
            parent2Phone = row['Phone No. 2']
            parent2ID = row['NRIC /ID 2']
            parent2Race = row['Race 2']
            parent2Citizenship = row['Citizenship 2']
            parent2Occupation = row['Occupation 2']
            parent2MainContact = row['Main contact 2']
            parent2AuthorisedPickUp = row['Authorised Pick Up Person 2']
            parent2EmailInvoiceReceipt = row['Email Invoice Receipt 2']
            parent2EmailCheckIn = row['Email checkin 2']

            parent2, created = Parent2.objects.update_or_create(
                child=child,
                defaults={
                    'parent2Relationship': parent2Relationship,
                    'parent2Name': parent2Name,
                    'parent2Email': parent2Email,
                    'parent2Mobile': parent2Mobile,
                    'parent2Phone': parent2Phone,
                    'parent2ID': parent2ID,
                    'parent2Race': parent2Race,
                    'parent2Citizenship': parent2Citizenship,
                    'parent2Occupation': parent2Occupation,
                    'parent2MainContact': parent2MainContact,
                    'parent2AuthorisedPickUp': parent2AuthorisedPickUp,
                    'parent2EmailInvoiceReceipt': parent2EmailInvoiceReceipt,
                    'parent2EmailCheckIn': parent2EmailCheckIn,
                }
            ) 

            parent3Relationship = row['Parent Relationship 3']
            parent3Name = row['Name 3']
            parent3Email = row['Email 3']
            parent3Mobile = row['Mobile No. 3']
            parent3Phone = row['Phone No. 3']
            parent3ID = row['NRIC /ID 3']
            parent3Race = row['Race 3']
            parent3Citizenship = row['Citizenship 3']
            parent3Occupation = row['Occupation 3']
            parent3MainContact = row['Main contact 3']
            parent3AuthorisedPickUp = row['Authorised Pick Up Person 3']
            parent3EmailInvoiceReceipt = row['Email Invoice Receipt 3']
            parent3EmailCheckIn = row['Email checkin 3']

            parent3, created = Parent3.objects.update_or_create(
                child=child,
                defaults={
                    'parent3Relationship': parent3Relationship,
                    'parent3Name': parent3Name,
                    'parent3Email': parent3Email,
                    'parent3Mobile': parent3Mobile,
                    'parent3Phone': parent3Phone,
                    'parent3ID': parent3ID,
                    'parent3Race': parent3Race,
                    'parent3Citizenship': parent3Citizenship,
                    'parent3Occupation': parent3Occupation,
                    'parent3MainContact': parent3MainContact,
                    'parent3AuthorisedPickUp': parent3AuthorisedPickUp,
                    'parent3EmailInvoiceReceipt': parent3EmailInvoiceReceipt,
                    'parent3EmailCheckIn': parent3EmailCheckIn,
                }
            ) 

            motherAddBlock = row['Mother Block no.']
            motherAddBuilding = row['Mother Building']
            motherAddStreet = row['Mother Street']
            motherAddUnit = row['Mother Unit']
            motherAddPostalCode = row['Mother Postal Code']
            motherAddTransport = row['Mother Transport Option']

            motherAdd, created = MotherAdd.objects.update_or_create(
                child=child,
                defaults={
                    'motherAddBlock': motherAddBlock,
                    'motherAddBuilding': motherAddBuilding,
                    'motherAddStreet': motherAddStreet,
                    'motherAddUnit': motherAddUnit,
                    'motherAddPostalCode': motherAddPostalCode,
                    'motherAddTransport': motherAddTransport,
                }
            ) 

            fatherAddBlock = row['Father Block no.']
            fatherAddBuilding = row['Father Building']
            fatherAddStreet = row['Father Street']
            fatherAddUnit = row['Father Unit']
            fatherAddPostalCode = row['Father Postal Code']
            fatherAddTransport = row['Father Transport Option']

            fatherAdd, created = FatherAdd.objects.update_or_create(
                child=child,
                defaults={
                    'fatherAddBlock': fatherAddBlock,
                    'fatherAddBuilding': fatherAddBuilding,
                    'fatherAddStreet': fatherAddStreet,
                    'fatherAddUnit': fatherAddUnit,
                    'fatherAddPostalCode': fatherAddPostalCode,
                    'fatherAddTransport': fatherAddTransport,
                }
            ) 

            address1Line1 = row['Residential Address Line 1']
            address1Line2 = row['Residential Address Line 2']
            address1PostalCode = row['Residential Postal Code']
            address1Transport = row['Residential Transport Option']

            address, created = Address.objects.update_or_create(
                child=child,
                defaults={
                    'address1Line1': address1Line1,
                    'address1Line2': address1Line2,
                    'address1PostalCode': address1PostalCode,
                    'address1Transport': address1Transport,
                }
            ) 

            emergency1Relationship = row['EC Relationship 1']
            emergency1Name = row['EC Name 1']
            emergency1Mobile = row['EC Mobile 1']
            emergency1Phone = row['EC Phone 1']
            emergency1Email = row['EC Email 1']

            emergency, created = Emergency.objects.update_or_create(
                child=child,
                defaults={
                    'emergency1Relationship': emergency1Relationship,
                    'emergency1Name': emergency1Name,
                    'emergency1Mobile': emergency1Mobile,
                    'emergency1Phone': emergency1Phone,
                    'emergency1Email': emergency1Email,
                }
            ) 
            
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
                temp_prifeesPaymentMethod=primary_fees.prifeesPaymentMethod if primary_fees else None,
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
                    phone=self.get_mobile_phone(temp.temp_parent1Mobile, temp.temp_parent1Phone),
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
                    phone=self.get_mobile_phone(temp.temp_parent2Mobile, temp.temp_parent2Phone),
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
                    phone=self.get_mobile_phone(temp.temp_parent3Mobile, temp.temp_parent3Phone),
                    email=temp.temp_parent3Email,
                    birthIC=temp.temp_parent3ID,
                    birthCountry=self.get_birthCode(temp.temp_parent3Citizenship),  
                    occupation=temp.temp_parent3Occupation,
                    relationship=temp.temp_parent3Relationship,
                    isAllowPickup=temp.temp_parent3MainContact,
                    isBillable=temp.temp_parent3AuthorisedPickUp,
                    isPrimary=temp.temp_parent3EmailInvoiceReceipt,
                    address=self.get_address_line(temp.temp_address1Line1, temp.temp_address1Line2), 
                    postcode=temp.temp_address1PostalCode, 
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

    def get_mobile_phone(self, mobile, phone): 
        if mobile:
            if mobile[0] == '1':
                if mobile[2] != '-':
                    mobile = mobile[:2] + '-' + mobile[2:]
                    return '0' + mobile
                elif mobile[2] == '-':
                    return '0' + mobile
            elif mobile[0] == '0':
                if mobile[3] != '-':
                    mobile = mobile[:3] + '-' + mobile[3:]
                    return mobile
                elif mobile[2] == '-':
                    return mobile

            return mobile

        elif phone:
            if phone[0] == '1':
                if phone[2] != '-':
                    phone = phone[:2] + '-' + phone[2:]
                    return '0' + phone
                elif phone[2] == '-':
                    return '0' + phone
            elif phone[0] == '0':
                if phone[3] != '-':
                    phone = phone[:3] + '-' + phone[3:]
                    return phone
                elif phone[2] == '-':
                    return phone

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

# Update CoreServiceChildrenMedicalContact Table
    def update_CSCMC_records(self):
        temporary_records = Temporary.objects.all()
        for temp in temporary_records:
            
            CoreServiceChildrenMedicalContact.objects.create(
                CSCMCTemporary=temp,
                CSCMCChild=temp.tempChild,
                name=temp.temp_emergency1Name,
                phone=self.get_mobile_phone(temp.temp_emergency1Mobile, temp.temp_emergency1Phone),
                child_id=temp.tempChild.id,
            )

# Read StaffList
    def read_staff_list(self, staff_csv_file):

        file = staff_csv_file.read().decode('utf-8').splitlines()
        data = file[1:]
        reader = csv.DictReader(data) # reader for non-header column, DictReader for header

        for row in reader:
					
            staff_name = row['Name']
            staff_email = row['Email']
            staff_gender = row['Gender']
            staff_dob = row['Dob']
            staff_title = row['Title']
            staff_mobileNum = row['Mobile Number']

            staff, created = Staff.objects.update_or_create(
                staff_email=staff_email,
                defaults={
                    'staff_name': staff_name,
                    'staff_gender': staff_gender,
                    'staff_dob': staff_dob,
                    'staff_title': staff_title,
                    'staff_mobileNum': staff_mobileNum,
                }
            )             
