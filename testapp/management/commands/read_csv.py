# testapp/management/commands/read_csv.py

# read_csv.py is to read Test CSV file.

# To run this command:
# python manage.py read_csv --test_csv=path/to/file.csv 

from django.core.management.base import BaseCommand
from testapp.models import Children, Family, Medical, Allergy
import csv
from datetime import datetime
from django.db import connection

class Command(BaseCommand):
    help = 'Read Test CSV file'

    def add_arguments(self, parser):
        parser.add_argument('--test_csv', type=str)

    def handle(self, *args, **kwargs):

        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE testapp_children_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE testapp_medical_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE testapp_family_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE testapp_allergy_id_seq RESTART WITH 1")

        if kwargs['test_csv']:
            self.read_csv(kwargs['test_csv'])

        self.stdout.write(self.style.SUCCESS('Read test.csv.'))        

    def read_csv(self, csv_file_path):
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:

                birthDate_fmt = row.get('birthDate', None)
                birthDate = None
                if birthDate_fmt:
                    try:
                        birthDate = datetime.strptime(birthDate_fmt, '%d/%m/%Y').date()
                    except ValueError:
                        self.stdout.write(self.style.ERROR(f'Invalid date format for {birthDate_fmt}. Skipping this row.'))
                        continue

                child, created = Children.objects.get_or_create(
                    branchId=row['branchId'],
                    firstName=row['firstName'],
                    lastName=row['lastName'],
                    defaults={
                        'fullName': row['fullName'],
                        'birthIC': row['birthIC'],
                        'birthDate': birthDate,
                        'birthCountry': row['birthCountry'],
                        'ethnicity': row['ethnicity'],
                        'religion': row['religion'],
                        'gender': row['gender'],
                        'age': row['age'],
                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'Children Table updated.'))
  
                medical, created = Medical.objects.update_or_create(
                    contactTypeMC=row['contactTypeMC'],
                    specialtyTypeMC=row['specialtyTypeMC'],
                    nameMC=row['nameMC'],
                    defaults={
                        'phoneMC': row['phoneMC'],
                        'addressMC': row['addressMC'],
                        'stateMC': row['stateMC'],
                        'countryMC': row['countryMC'],
                        'postcodeMC': row['postcodeMC'],
                        'children': child,
                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'Medical Table updated.'))

                family, created = Family.objects.update_or_create(
                    firstNameFamily=row['firstNameFamily'],
                    lastNameFamily=row['lastNameFamily'],
                    defaults={
                        'phoneFamily': row['phoneFamily'],
                        'emailFamily': row['emailFamily'],
                        'birthICFamily': row['birthICFamily'],
                        'birthCountryFamily': row['birthCountryFamily'],
                        'occupationFamily': row['occupationFamily'],
                        'relationshipFamily': row['relationshipFamily'],
                        'addressFamily': row['addressFamily'],
                        'stateFamily': row['stateFamily'],
                        'countryFamily': row['countryFamily'],
                        'postcodeFamily': row['postcodeFamily'],
                        'isAllowPickup': row['isAllowPickup'],
                        'children': child,
                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'Family Table updated.'))

                allergy, created = Allergy.objects.update_or_create(
                    allergyType=row['allergyType'],
                    allergies=row['allergies'],
                    defaults={
                        'allergicPrevent': row['allergicPrevent'],
                        'allergicSyndrome': row['allergicSyndrome'],
                        'allergicAction': row['allergicAction'],
                        'haveMedicine': row['haveMedicine'],
                        'children': child,
                    }
                ) 
                self.stdout.write(self.style.SUCCESS(f'Allergy Table updated.'))


