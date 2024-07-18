from django.db import models

class Child(models.Model):

    OPTION_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    childNo = models.CharField(max_length=100)
    childName = models.CharField(max_length=100)
    childForeignName = models.CharField(max_length=100, blank=True)
    childBirthID = models.CharField(max_length=100)
    childGender = models.CharField(max_length=100)
    childDOB = models.CharField(blank=True)
    childAge = models.CharField(max_length=100, blank=True)
    childRace = models.CharField(max_length=100, blank=True)
    childCitizenship = models.CharField(max_length=100, blank=True)
    childResidentialStatus = models.CharField(max_length=100, blank=True)
    childReligion = models.CharField(max_length=100, blank=True)
    childMTLanguage = models.CharField(max_length=100, blank=True)
    childToStaff = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
    childHouseholdIncome = models.CharField(max_length=100, blank=True)
    childSubsidyType = models.CharField(max_length=100, blank=True)
    childResidentialRemarks = models.CharField(max_length=100, blank=True)

class Siblings(models.Model):
    siblings1 = models.CharField(max_length=100, blank=True)
    siblingsRelationship1 = models.CharField(max_length=100, blank=True)
    siblings2 = models.CharField(max_length=100, blank=True)
    siblingsRelationship2 = models.CharField(max_length=100, blank=True)
    siblings3 = models.CharField(max_length=100, blank=True)
    siblingsRelationship3 = models.CharField(max_length=100, blank=True)
    siblings4 = models.CharField(max_length=100, blank=True)
    siblingsRelationship4 = models.CharField(max_length=100, blank=True)

    child = models.ForeignKey(Child, on_delete=models.CASCADE)

class Health(models.Model):
    healthMedCon = models.CharField(max_length=100, blank=True)
    healthVaccination = models.CharField(max_length=100, blank=True)
    healthAllergy = models.CharField(max_length=100, blank=True)
    healthSpecialDiet = models.CharField(max_length=100, blank=True)
    healthSpecialNeeds = models.CharField(max_length=100, blank=True)
    healthFamDrNo = models.CharField(max_length=100, blank=True)

    child = models.ForeignKey(Child, on_delete=models.CASCADE)

class School(models.Model):
    schoolAdmissionDate = models.CharField(max_length=100, blank=True)
    schoolWithdrawalDate = models.CharField(max_length=100, blank=True)
    schoolProgramType = models.CharField(max_length=100, blank=True)
    schoolClassname = models.CharField(max_length=100, blank=True)
    schoolClassSession = models.CharField(max_length=100, blank=True)
    schoolClassLevel = models.CharField(max_length=100, blank=True)
    schoolTransportationNo = models.CharField(max_length=100, blank=True)

    child = models.ForeignKey(Child, on_delete=models.CASCADE)

class PrimaryFees(models.Model):
    prieesPaymentMethod = models.CharField(max_length=100, blank=True)
    prifeesBankName = models.CharField(max_length=100, blank=True)
    prifeesBankAccHolder = models.CharField(max_length=100, blank=True)
    prifeesBankAccCode = models.CharField(max_length=100, blank=True)
    prifeesBranchCode = models.CharField(max_length=100, blank=True)
    prifeesBankAccNumber = models.CharField(max_length=100, blank=True)
    prifeesApprovalDate = models.CharField(max_length=100, blank=True)
    prifeesAttentionTo = models.CharField(max_length=100, blank=True)
    prifeesPayeeID = models.CharField(max_length=100, blank=True)
    prifeesAmount = models.CharField(max_length=100, blank=True)

    child = models.ForeignKey(Child, on_delete=models.CASCADE)

class SecondaryFees(models.Model):
    secfeesPaymentMethod = models.CharField(max_length=100, blank=True)
    secfeesBankName = models.CharField(max_length=100, blank=True)
    secfeesBankAccHolder = models.CharField(max_length=100, blank=True)
    secfeesBankAccCode = models.CharField(max_length=100, blank=True)
    secfeesBranchCode = models.CharField(max_length=100, blank=True)
    secfeesBankAccNo = models.CharField(max_length=100, blank=True)
    secfeesPayeeID = models.CharField(max_length=100, blank=True)
    secfeesApprovalDate = models.CharField(blank=True)
    secfeesAttentionTo = models.CharField(max_length=100, blank=True)

    child = models.ForeignKey(Child, on_delete=models.CASCADE)

class Refund(models.Model):
    refundPaymentMethod = models.CharField(max_length=100, blank=True)
    refundBankName = models.CharField(max_length=100, blank=True)
    refundBankAccHolder = models.CharField(max_length=100, blank=True)
    refundBankAccCode = models.CharField(max_length=100, blank=True)
    refundBranchCode = models.CharField(max_length=100, blank=True)
    refundBankAccNo = models.CharField(max_length=100, blank=True)
    refundApprovalReference = models.CharField(max_length=100, blank=True)
    refundApprovalDate = models.CharField(max_length=100, blank=True)
    refundDepositOpt = models.CharField(max_length=100, blank=True)

    child = models.ForeignKey(Child, on_delete=models.CASCADE)

class Parent1(models.Model):

    OPTION_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    parent1Relationship = models.CharField(max_length=100, blank=True)
    parent1Name = models.CharField(max_length=100, blank=True)
    parent1Email = models.CharField(max_length=100, blank=True)
    parent1Mobile = models.CharField(max_length=100, blank=True)
    parent1Phone = models.CharField(max_length=100, blank=True)
    parent1ID = models.CharField(max_length=100, blank=True)
    parent1Race = models.CharField(max_length=100, blank=True)
    parent1Citizenship = models.CharField(max_length=100, blank=True)
    parent1Occupation = models.CharField(max_length=100, blank=True)
    parent1MainContact = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
    parent1AuthorisedPickUp = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
    parent1EmailInvoiceReceipt = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
    parent1EmailCheckIn = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)

    child = models.ForeignKey(Child, on_delete=models.CASCADE)

class Parent2(models.Model):

    OPTION_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    parent2Relationship = models.CharField(max_length=100, blank=True)
    parent2Name = models.CharField(max_length=100, blank=True)
    parent2Email = models.CharField(max_length=100, blank=True)
    parent2Mobile = models.CharField(max_length=100, blank=True)
    parent2Phone = models.CharField(max_length=100, blank=True)
    parent2ID = models.CharField(max_length=100, blank=True)
    parent2Race = models.CharField(max_length=100, blank=True)
    parent2Citizenship = models.CharField(max_length=100, blank=True)
    parent2Occupation = models.CharField(max_length=100, blank=True)
    parent2MainContact = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
    parent2AuthorisedPickUp = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
    parent2EmailInvoiceReceipt = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
    parent2EmailCheckIn = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)

    child = models.ForeignKey(Child, on_delete=models.CASCADE)

class Parent3(models.Model):

    OPTION_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    parent3Relationship = models.CharField(max_length=100, blank=True)
    parent3Name = models.CharField(max_length=100, blank=True)
    parent3Email = models.CharField(max_length=100, blank=True)
    parent3Mobile = models.CharField(max_length=100, blank=True)
    parent3Phone = models.CharField(max_length=100, blank=True)
    parent3ID = models.CharField(max_length=100, blank=True)
    parent3Race = models.CharField(max_length=100, blank=True)
    parent3Citizenship = models.CharField(max_length=100, blank=True)
    parent3Occupation = models.CharField(max_length=100, blank=True)
    parent3MainContact = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
    parent3AuthorisedPickUp = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
    parent3EmailInvoiceReceipt = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
    parent3EmailCheckIn = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)

    child = models.ForeignKey(Child, on_delete=models.CASCADE)

class MotherAdd(models.Model):
    motherAddBlock = models.CharField(max_length=100, blank=True)
    motherAddBuilding = models.CharField(max_length=100, blank=True)
    motherAddStreet = models.CharField(max_length=100, blank=True)
    motherAddUnit = models.CharField(max_length=100, blank=True)
    motherAddPostalCode = models.CharField(max_length=100, blank=True)
    motherAddTransport = models.CharField(max_length=100, blank=True)

    child = models.ForeignKey(Child, on_delete=models.CASCADE)

class FatherAdd(models.Model):
    fatherAddBlock = models.CharField(max_length=100, blank=True)
    fatherAddBuilding = models.CharField(max_length=100, blank=True)
    fatherAddStreet = models.CharField(max_length=100, blank=True)
    fatherAddUnit = models.CharField(max_length=100, blank=True)
    fatherAddPostalCode = models.CharField(max_length=100, blank=True)
    fatherAddTransport = models.CharField(max_length=100, blank=True)

    child = models.ForeignKey(Child, on_delete=models.CASCADE)

class Address(models.Model):
    address1Line1 = models.CharField(max_length=100, blank=True)
    address1Line2 = models.CharField(max_length=100, blank=True)
    address1PostalCode = models.CharField(max_length=100, blank=True)
    address1Transport = models.CharField(max_length=100, blank=True)

    child = models.ForeignKey(Child, on_delete=models.CASCADE)

class Emergency(models.Model):
    emergency1Relationship = models.CharField(max_length=100, blank=True)
    emergency1Name = models.CharField(max_length=100, blank=True)
    emergency1Mobile = models.CharField(max_length=100, blank=True)
    emergency1Phone = models.CharField(max_length=100, blank=True)
    emergency1Email = models.CharField(max_length=100, blank=True)

    child = models.ForeignKey(Child, on_delete=models.CASCADE)

class Temporary(models.Model):
    tempChild  = models.OneToOneField(Child, on_delete=models.CASCADE, blank=True)
    tempSiblings = models.OneToOneField(Siblings, on_delete=models.CASCADE, blank=True)
    tempHealth = models.OneToOneField(Health, on_delete=models.CASCADE, blank=True)
    tempSchool  = models.OneToOneField(School, on_delete=models.CASCADE, blank=True)
    tempPrimaryFees = models.OneToOneField(PrimaryFees, on_delete=models.CASCADE, blank=True)
    tempSecondaryFees = models.OneToOneField(SecondaryFees, on_delete=models.CASCADE, blank=True)
    tempRefund  = models.OneToOneField(Refund, on_delete=models.CASCADE, blank=True)
    tempParent1 = models.OneToOneField(Parent1, on_delete=models.CASCADE, blank=True)
    tempParent2 = models.OneToOneField(Parent2, on_delete=models.CASCADE, blank=True)
    tempParent3  = models.OneToOneField(Parent3, on_delete=models.CASCADE, blank=True)
    tempMotherAdd = models.OneToOneField(MotherAdd, on_delete=models.CASCADE, blank=True)
    tempFatherAdd = models.OneToOneField(FatherAdd, on_delete=models.CASCADE, blank=True)
    tempAddress  = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True)
    tempEmergency = models.OneToOneField(Emergency, on_delete=models.CASCADE, blank=True)
