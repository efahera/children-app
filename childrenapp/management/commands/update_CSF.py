# update_CSF.py

from django.core.management.base import BaseCommand
from childrenapp.models import Child, Siblings, Health, School, PrimaryFees, SecondaryFees, Refund, Parent1, Parent2, Parent3, MotherAdd, FatherAdd, Address, Emergency, Temporary, CoreServiceFamily
from django.db import connection

class Command(BaseCommand):
    help = 'Update CoreServiceFamily from Temporary'

    def handle(self, *args, **kwargs):
        CoreServiceFamily.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE childrenapp_coreservicefamily_id_seq RESTART WITH 1")
        
        self.update_CSF_records()
        self.stdout.write(self.style.SUCCESS('Successfully updated CoreServiceFamily records'))

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
