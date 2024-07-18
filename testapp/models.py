from django.db import models

class Children(models.Model):
    ETHNICITY_CHOICES = [
        ('Malay', 'Malay'),
        ('Chinese', 'Chinese'),
        ('Indian', 'Indian'),
        ('Others', 'Others'),
    ]

    RELIGION_CHOICES = [
        ('Islam', 'Islam'),
        ('Buddhism', 'Buddhism'),
        ('Hinduism', 'Hinduism'),
        ('Christianity', 'Christianity'),
        ('Others', 'Others'),
    ]
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    branchId = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    fullName = models.CharField(max_length=100)
    birthIC = models.CharField(max_length=12)
    birthDate = models.DateField()
    birthCountry = models.CharField(max_length=50)
    ethnicity = models.CharField(max_length=50, choices=ETHNICITY_CHOICES)
    religion = models.CharField(max_length=50, choices=RELIGION_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    
    def __str__(self):
        return f'ID: {self.branchId} - Name: {self.firstName} {self.lastName}'

class Medical(models.Model):
    contactTypeMC = models.CharField(max_length=50)
    specialtyTypeMC = models.CharField(max_length=50)
    nameMC = models.CharField(max_length=50)
    phoneMC = models.CharField(max_length=15)
    addressMC = models.CharField(max_length=100)
    stateMC = models.CharField(max_length=50)
    countryMC = models.CharField(max_length=50)
    postcodeMC = models.CharField(max_length=10)

    children = models.ForeignKey(Children, on_delete=models.CASCADE)

    def __str__(self):
        return f'Name: {self.children.fullName}, Medical contact: {self.nameMC} ({self.phoneMC})'

class Family(models.Model):
    PICKUP_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]

    firstNameFamily = models.CharField(max_length=50)
    lastNameFamily = models.CharField(max_length=50)
    phoneFamily = models.CharField(max_length=15)
    emailFamily = models.CharField(max_length=50)
    birthICFamily = models.CharField(max_length=12)
    birthCountryFamily = models.CharField(max_length=30)
    occupationFamily = models.CharField(max_length=20)
    relationshipFamily = models.CharField(max_length=20)
    addressFamily = models.CharField(max_length=100)
    stateFamily = models.CharField(max_length=50)
    countryFamily = models.CharField(max_length=50)
    postcodeFamily = models.CharField(max_length=10)
    isAllowPickup = models.CharField(max_length=3, choices=PICKUP_CHOICES)

    children = models.ForeignKey(Children, on_delete=models.CASCADE)
 
    def __str__(self):
        return f'Name: {self.children.fullName}, {self.relationshipFamily}: {self.firstNameFamily} {self.lastNameFamily} ({self.relationshipFamily})'

class Allergy(models.Model):
    MEDICINE_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]

    allergyType = models.CharField(max_length=30)
    allergies = models.CharField(max_length=30)
    allergicPrevent = models.CharField(max_length=30)
    allergicSyndrome = models.CharField(max_length=30)
    allergicAction = models.CharField(max_length=30)
    haveMedicine = models.CharField(max_length=3, choices=MEDICINE_CHOICES)

    children = models.ForeignKey(Children, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Name: {self.children.fullName}, Allergy: {self.allergies}'

