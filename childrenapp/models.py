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
    childDOB = models.CharField(max_length=100, blank=True)
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
    prifeesPaymentMethod = models.CharField(max_length=100, blank=True)
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
    secfeesApprovalDate = models.CharField(max_length=100, blank=True)
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

        OPTION_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

        tempChild  = models.ForeignKey(Child, on_delete=models.CASCADE, blank=True)
        temp_childNo = models.CharField(max_length=100, blank=True)
        temp_childName = models.CharField(max_length=100, blank=True)
        temp_childForeignName = models.CharField(max_length=100, blank=True)
        temp_childBirthID = models.CharField(max_length=100, blank=True)
        temp_childGender = models.CharField(max_length=100, blank=True)
        temp_childDOB = models.CharField(max_length=100, blank=True)
        temp_childAge = models.CharField(max_length=100, blank=True)
        temp_childRace = models.CharField(max_length=100, blank=True)
        temp_childCitizenship = models.CharField(max_length=100, blank=True)
        temp_childResidentialStatus = models.CharField(max_length=100, blank=True)
        temp_childReligion = models.CharField(max_length=100, blank=True)
        temp_childMTLanguage = models.CharField(max_length=100, blank=True)
        temp_childToStaff = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
        temp_childHouseholdIncome = models.CharField(max_length=100, blank=True)
        temp_childSubsidyType = models.CharField(max_length=100, blank=True)
        temp_childResidentialRemarks = models.CharField(max_length=100, blank=True)
    
        tempSiblings = models.ForeignKey(Siblings, on_delete=models.CASCADE, blank=True)
        temp_siblings1 = models.CharField(max_length=100, blank=True)
        temp_siblingsRelationship1 = models.CharField(max_length=100, blank=True)
        temp_siblings2 = models.CharField(max_length=100, blank=True)
        temp_siblingsRelationship2 = models.CharField(max_length=100, blank=True)
        temp_siblings3 = models.CharField(max_length=100, blank=True)
        temp_siblingsRelationship3 = models.CharField(max_length=100, blank=True)
        temp_siblings4 = models.CharField(max_length=100, blank=True)
        temp_siblingsRelationship4 = models.CharField(max_length=100, blank=True)

        tempHealth = models.ForeignKey(Health, on_delete=models.CASCADE, blank=True)
        temp_healthMedCon = models.CharField(max_length=100, blank=True)
        temp_healthVaccination = models.CharField(max_length=100, blank=True)
        temp_healthAllergy = models.CharField(max_length=100, blank=True)
        temp_healthSpecialDiet = models.CharField(max_length=100, blank=True)
        temp_healthSpecialNeeds = models.CharField(max_length=100, blank=True)
        temp_healthFamDrNo = models.CharField(max_length=100, blank=True)

        tempSchool  = models.ForeignKey(School, on_delete=models.CASCADE, blank=True)
        temp_schoolAdmissionDate = models.CharField(max_length=100, blank=True)
        temp_schoolWithdrawalDate = models.CharField(max_length=100, blank=True)
        temp_schoolProgramType = models.CharField(max_length=100, blank=True)
        temp_schoolClassname = models.CharField(max_length=100, blank=True)
        temp_schoolClassSession = models.CharField(max_length=100, blank=True)
        temp_schoolClassLevel = models.CharField(max_length=100, blank=True)
        temp_schoolTransportationNo = models.CharField(max_length=100, blank=True)

        tempPrimaryFees = models.ForeignKey(PrimaryFees, on_delete=models.CASCADE, blank=True)
        temp_prifeesPaymentMethod = models.CharField(max_length=100, blank=True)
        temp_prifeesBankName = models.CharField(max_length=100, blank=True)
        temp_prifeesBankAccHolder = models.CharField(max_length=100, blank=True)
        temp_prifeesBankAccCode = models.CharField(max_length=100, blank=True)
        temp_prifeesBranchCode = models.CharField(max_length=100, blank=True)
        temp_prifeesBankAccNumber = models.CharField(max_length=100, blank=True)
        temp_prifeesApprovalDate = models.CharField(max_length=100, blank=True)
        temp_prifeesAttentionTo = models.CharField(max_length=100, blank=True)
        temp_prifeesPayeeID = models.CharField(max_length=100, blank=True)
        temp_prifeesAmount = models.CharField(max_length=100, blank=True)

        tempSecondaryFees = models.ForeignKey(SecondaryFees, on_delete=models.CASCADE, blank=True)
        temp_secfeesPaymentMethod = models.CharField(max_length=100, blank=True)
        temp_secfeesBankName = models.CharField(max_length=100, blank=True)
        temp_secfeesBankAccHolder = models.CharField(max_length=100, blank=True)
        temp_secfeesBankAccCode = models.CharField(max_length=100, blank=True)
        temp_secfeesBranchCode = models.CharField(max_length=100, blank=True)
        temp_secfeesBankAccNo = models.CharField(max_length=100, blank=True)
        temp_secfeesPayeeID = models.CharField(max_length=100, blank=True)
        temp_secfeesApprovalDate = models.CharField(max_length=100, blank=True)
        temp_secfeesAttentionTo = models.CharField(max_length=100, blank=True)

        tempRefund  = models.ForeignKey(Refund, on_delete=models.CASCADE, blank=True)
        temp_refundPaymentMethod = models.CharField(max_length=100, blank=True)
        temp_refundBankName = models.CharField(max_length=100, blank=True)
        temp_refundBankAccHolder = models.CharField(max_length=100, blank=True)
        temp_refundBankAccCode = models.CharField(max_length=100, blank=True)
        temp_refundBranchCode = models.CharField(max_length=100, blank=True)
        temp_refundBankAccNo = models.CharField(max_length=100, blank=True)
        temp_refundApprovalReference = models.CharField(max_length=100, blank=True)
        temp_refundApprovalDate = models.CharField(max_length=100, blank=True)
        temp_refundDepositOpt = models.CharField(max_length=100, blank=True)

        tempParent1 = models.ForeignKey(Parent1, on_delete=models.CASCADE, blank=True)
        temp_parent1Relationship = models.CharField(max_length=100, blank=True)
        temp_parent1Name = models.CharField(max_length=100, blank=True)
        temp_parent1Email = models.CharField(max_length=100, blank=True)
        temp_parent1Mobile = models.CharField(max_length=100, blank=True)
        temp_parent1Phone = models.CharField(max_length=100, blank=True)
        temp_parent1ID = models.CharField(max_length=100, blank=True)
        temp_parent1Race = models.CharField(max_length=100, blank=True)
        temp_parent1Citizenship = models.CharField(max_length=100, blank=True)
        temp_parent1Occupation = models.CharField(max_length=100, blank=True)
        temp_parent1MainContact = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
        temp_parent1AuthorisedPickUp = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
        temp_parent1EmailInvoiceReceipt = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
        temp_parent1EmailCheckIn = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)

        tempParent2 = models.ForeignKey(Parent2, on_delete=models.CASCADE, blank=True)
        temp_parent2Relationship = models.CharField(max_length=100, blank=True)
        temp_parent2Name = models.CharField(max_length=100, blank=True)
        temp_parent2Email = models.CharField(max_length=100, blank=True)
        temp_parent2Mobile = models.CharField(max_length=100, blank=True)
        temp_parent2Phone = models.CharField(max_length=100, blank=True)
        temp_parent2ID = models.CharField(max_length=100, blank=True)
        temp_parent2Race = models.CharField(max_length=100, blank=True)
        temp_parent2Citizenship = models.CharField(max_length=100, blank=True)
        temp_parent2Occupation = models.CharField(max_length=100, blank=True)
        temp_parent2MainContact = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
        temp_parent2AuthorisedPickUp = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
        temp_parent2EmailInvoiceReceipt = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
        temp_parent2EmailCheckIn = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)

        tempParent3  = models.ForeignKey(Parent3, on_delete=models.CASCADE, blank=True)
        temp_parent3Relationship = models.CharField(max_length=100, blank=True)
        temp_parent3Name = models.CharField(max_length=100, blank=True)
        temp_parent3Email = models.CharField(max_length=100, blank=True)
        temp_parent3Mobile = models.CharField(max_length=100, blank=True)
        temp_parent3Phone = models.CharField(max_length=100, blank=True)
        temp_parent3ID = models.CharField(max_length=100, blank=True)
        temp_parent3Race = models.CharField(max_length=100, blank=True)
        temp_parent3Citizenship = models.CharField(max_length=100, blank=True)
        temp_parent3Occupation = models.CharField(max_length=100, blank=True)
        temp_parent3MainContact = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
        temp_parent3AuthorisedPickUp = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
        temp_parent3EmailInvoiceReceipt = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)
        temp_parent3EmailCheckIn = models.CharField(max_length=100, blank=True, choices=OPTION_CHOICES)

        tempMotherAdd = models.ForeignKey(MotherAdd, on_delete=models.CASCADE, blank=True)
        temp_motherAddBlock = models.CharField(max_length=100, blank=True)
        temp_motherAddBuilding = models.CharField(max_length=100, blank=True)
        temp_motherAddStreet = models.CharField(max_length=100, blank=True)
        temp_motherAddUnit = models.CharField(max_length=100, blank=True)
        temp_motherAddPostalCode = models.CharField(max_length=100, blank=True)
        temp_motherAddTransport = models.CharField(max_length=100, blank=True)

        tempFatherAdd = models.ForeignKey(FatherAdd, on_delete=models.CASCADE, blank=True)
        temp_fatherAddBlock = models.CharField(max_length=100, blank=True)
        temp_fatherAddBuilding = models.CharField(max_length=100, blank=True)
        temp_fatherAddStreet = models.CharField(max_length=100, blank=True)
        temp_fatherAddUnit = models.CharField(max_length=100, blank=True)
        temp_fatherAddPostalCode = models.CharField(max_length=100, blank=True)
        temp_fatherAddTransport = models.CharField(max_length=100, blank=True)

        tempAddress  = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True)
        temp_address1Line1 = models.CharField(max_length=100, blank=True)
        temp_address1Line2 = models.CharField(max_length=100, blank=True)
        temp_address1PostalCode = models.CharField(max_length=100, blank=True)
        temp_address1Transport = models.CharField(max_length=100, blank=True)

        tempEmergency = models.ForeignKey(Emergency, on_delete=models.CASCADE, blank=True)
        temp_emergency1Relationship = models.CharField(max_length=100, blank=True)
        temp_emergency1Name = models.CharField(max_length=100, blank=True)
        temp_emergency1Mobile = models.CharField(max_length=100, blank=True)
        temp_emergency1Phone = models.CharField(max_length=100, blank=True)
        temp_emergency1Email = models.CharField(max_length=100, blank=True)

class CoreServiceFamily(models.Model):

    # Parent
    userId = models.CharField(max_length=250, blank=True)
    firstName = models.CharField(max_length=250, blank=True)
    lastName = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=250, blank=True)
    email = models.CharField(max_length=250, blank=True)
    gender = models.CharField(max_length=250, blank=True)
    birthIC = models.CharField(max_length=250, blank=True)
    birthCountry = models.CharField(max_length=250, blank=True)
    occupation = models.CharField(max_length=250, blank=True)
    relationship = models.CharField(max_length=250, blank=True)
    profileImage = models.CharField(max_length=250, blank=True)

    # Parent Address
    address = models.CharField(max_length=250, blank=True)
    state = models.CharField(max_length=250, blank=True)
    country = models.CharField(max_length=250, blank=True)
    postcode = models.CharField(max_length=250, blank=True)

    # Parent
    isArchived = models.CharField(max_length=250, blank=True)
    isAllowPickup = models.CharField(max_length=250, blank=True)
    isEmergencyContact = models.CharField(max_length=250, blank=True)
    isBillable = models.CharField(max_length=250, blank=True)
    isPrimary = models.CharField(max_length=250, blank=True)
    isWebAccess = models.CharField(max_length=250, blank=True)
    isMobileAccess = models.CharField(max_length=250, blank=True)

    # Auto add
    creator = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField("createdAt", auto_now_add=True)
    updated_at = models.DateTimeField("updatedAt", auto_now=True)

    # Foreign Key
    CSFTemporary = models.ForeignKey(Temporary, on_delete=models.CASCADE, blank=True, null=True)
    CSFChild = models.ForeignKey(Child, on_delete=models.CASCADE, blank=True, null=True)

class CoreServiceChildrenMedicalContact(models.Model):

    userId = models.CharField(max_length=250, blank=True)
    contactType = models.CharField(max_length=250, blank=True)
    specialtyType = models.CharField(max_length=250, blank=True)
    name = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=250, blank=True)
    address = models.CharField(max_length=250, blank=True)
    state = models.CharField(max_length=250, blank=True)
    country = models.CharField(max_length=250, blank=True)
    postcode = models.CharField(max_length=250, blank=True)
    notes = models.CharField(max_length=250, blank=True)
    enterBy = models.CharField(max_length=250, blank=True)
    createdAt = models.DateTimeField("createdAt", auto_now_add=True)
    updatedAt = models.DateTimeField("updatedAt", auto_now=True)
    child_id = models.CharField(max_length=250, blank=True)
    isArchived = models.CharField(max_length=250, blank=True)

    # Foreign Key
    CSCMCTemporary = models.ForeignKey(Temporary, on_delete=models.CASCADE, blank=True, null=True)
    CSCMCChild = models.ForeignKey(Child, on_delete=models.CASCADE, blank=True, null=True)

class Staff(models.Model):

    staff_name = models.CharField(max_length=250, blank=True)
    staff_email = models.CharField(max_length=250, blank=True)
    staff_gender = models.CharField(max_length=250, blank=True)
    staff_dob = models.CharField(max_length=250, blank=True)
    staff_title = models.CharField(max_length=250, blank=True)
    staff_mobileNum = models.CharField(max_length=250, blank=True)

# class CoreServiceChildren(models.Model):

#     id
#     createdAt
#     updatedAt
#     tenantId
#     branchId
#     firstName
#     lastName
#     fullName
#     birthCertNo
#     birthIC
#     birthDate
#     birthOrder
#     birthCountry
#     ethnicity
#     religion
#     siblings
#     profileImage
#     gender
#     age
#     isActive
#     isArchived
#     notes
#     isEnRolled
#     admissionId
#     isPresentToday
#     isInToday
#     isOutToday
#     isWithdraw
#     isMarkedWithdraw
#     withDrawDate
#     withDrawReason
#     isMarkedPromote
#     PromoteDate
#     PromoteReason
#     creator

# class CoreServiceChildrenSibling(models.Model):

#     id
#     child_id
#     sibling_id

# class CoreServiceChildrenAllergies(models.Model):

#     id
#     allergyType
#     allergies
#     allergicPrevent
#     allergicSyndrome
#     allergicAction
#     haveMedicine
#     enterBy
#     created_at
#     updated_at
#     child_id

# class CoreServiceChildrenMedicines(models.Model):

#     id
#     type
#     name
#     purpose
#     dosage
#     carriedBy
#     isForAllergic
#     remarks
#     enterBy
#     createdAt
#     updatedAt
#     allergic_id
#     child_id
#     endDate
#     frequency
#     startDate
#     medTime
#     takenWhen
#     isArchived

# class CoreServiceChildrenEnrollment(models.Model):

#     id
#     tenantId
#     branchId
#     academyYear
#     enrollStartDate
#     enrollEndDate
#     status
#     active
#     isSpecial
#     notes
#     enrollBy
#     created_at
#     updated_at
#     children_id
#     classroom_id
#     program_id

# class CoreServiceClassrooms(models.Model):

#     id
#     createdAt
#     updatedAt
#     tenantId
#     branchId
#     name
#     maxCapacity
#     availableCapacity
#     academyYear
#     isSpecial
#     active
#     isArchived
#     enteredBy
#     programs_id

# class CoreServiceClassroomChildren(models.Model):

#     id
#     createdAt
#     updatedAt
#     tenantId
#     branchId
#     academyYear
#     academyMonth
#     isSpecial
#     isActive
#     isArchived
#     isMarkedWithdraw
#     withDrawDate
#     withDrawReason
#     isMarkedPromote
#     PromoteDate
#     PromoteReason
#     createdAt1
#     updatedAt1
#     assignedBy_id
#     child_id
#     classroom_id

# class CoreServiceChildrenFamily(models.Model):

#     id
#     tenantId
#     branchId
#     child_id
#     user_id
#     family_id

