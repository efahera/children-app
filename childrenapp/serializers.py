from rest_framework import serializers
from .models import Child, Siblings, Health, School, PrimaryFees, SecondaryFees, Refund, Parent1, Parent2, Parent3, MotherAdd, FatherAdd, Address, Emergency, Temporary

class ChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
        fields = '__all__'

class SiblingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Siblings
        fields = '__all__'

class HealthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Health 
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class PrimaryFeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrimaryFees
        fields = '__all__'

class SecondaryFeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SecondaryFees
        fields = '__all__'

class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = '__all__'

class Parent1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Parent1
        fields = '__all__'

class Parent2Serializer(serializers.ModelSerializer):

    class Meta:
        model = Parent2
        fields = '__all__'

class Parent3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Parent3
        fields = '__all__'

class MotherAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = MotherAdd
        fields = '__all__'

class FatherAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = FatherAdd
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class EmergencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Emergency
        fields = '__all__'

class TemporarySerializer(serializers.ModelSerializer):

    # child serializer
        temp_childNo = models.CharField(source='tempChild.childNo')
        temp_childName = models.CharField(source='tempChild.childName')
        temp_childForeignName = models.CharField(source='tempChild.childForeignName')
        temp_childBirthID = models.CharField(source='tempChild.childBirthID')
        temp_childGender = models.CharField(source='tempChild.childGender')
        temp_childDOB = models.CharField(source='tempChild.childDOB')
        temp_childAge = models.CharField(source='tempChild.childAge')
        temp_childRace = models.CharField(source='tempChild.childRace')
        temp_childCitizenship = models.CharField(source='tempChild.childCitizenship')
        temp_childResidentialStatus = models.CharField(source='tempChild.childResidentialStatus')
        temp_childReligion = models.CharField(source='tempChild.childReligion')
        temp_childMTLanguage = models.CharField(source='tempChild.childMTLanguage')
        temp_childToStaff = models.CharField(source='tempChild.childToStaff')
        temp_childHouseholdIncome = models.CharField(source='tempChild.childHouseholdIncome')
        temp_childSubsidyType = models.CharField(source='tempChild.childSubsidyType')
        temp_childResidentialRemarks = models.CharField(source='tempChild.childResidentialRemarks')

    # siblings serializer
        temp_siblings1 = models.CharField(source='tempSiblings.siblings1')
        temp_siblings2 = models.CharField(source='tempSiblings.siblings2')
        temp_siblings3 = models.CharField(source='tempSiblings.siblings3')
        temp_siblings4 = models.CharField(source='tempSiblings.siblings4')
        temp_siblingsRelationship1 = models.CharField(source='tempSiblings.siblingsRelationship1')
        temp_siblingsRelationship2 = models.CharField(source='tempSiblings.siblingsRelationship2')
        temp_siblingsRelationship3 = models.CharField(source='tempSiblings.siblingsRelationship3')
        temp_siblingsRelationship4 = models.CharField(source='tempSiblings.siblingsRelationship4')

    # health serializer
        temp_healthMedCon = models.CharField(source='tempHealth.healthMedCon')
        temp_healthVaccination = models.CharField(source='tempHealth.healthVaccination')
        temp_healthAllergy = models.CharField(source='tempHealth.healthAllergy')
        temp_healthSpecialDiet = models.CharField(source='tempHealth.healthSpecialDiet')
        temp_healthSpecialNeeds = models.CharField(source='tempHealth.healthSpecialNeeds')
        temp_healthFamDrNo = models.CharField(source='tempHealth.healthFamDrNo')

    # school serializer
        temp_schoolAdmissionDate = models.CharField(source='tempSchool.schoolAdmissionDate')
        temp_schoolWithdrawalDate = models.CharField(source='tempSchool.schoolWithdrawalDate')
        temp_schoolProgramType = models.CharField(source='tempSchool.schoolProgramType')
        temp_schoolClassname = models.CharField(source='tempSchool.schoolClassname')
        temp_schoolClassSession = models.CharField(source='tempSchool.schoolClassSession')
        temp_schoolClassLevel = models.CharField(source='tempSchool.schoolClassLevel')
        temp_schoolTransportationNo = models.CharField(source='tempSchool.schoolTransportationNo')

    # primary fees serializer
        temp_prieesPaymentMethod = models.CharField(source='tempPrimaryFees.prieesPaymentMethod')
        temp_prifeesBankName = models.CharField(source='tempPrimaryFees.prifeesBankName')
        temp_prifeesBankAccHolder = models.CharField(source='tempPrimaryFees.prifeesBankAccHolder')
        temp_prifeesBankAccCode = models.CharField(source='tempPrimaryFees.prifeesBankAccCode')
        temp_prifeesBranchCode = models.CharField(source='tempPrimaryFees.prifeesBranchCode')
        temp_prifeesBankAccNumber = models.CharField(source='tempPrimaryFees.prifeesBankAccNumber')
        temp_prifeesApprovalDate = models.CharField(source='tempPrimaryFees.prifeesApprovalDate')
        temp_prifeesAttentionTo = models.CharField(source='tempPrimaryFees.prifeesAttentionTo')
        temp_prifeesPayeeID = models.CharField(source='tempPrimaryFees.prifeesPayeeID')
        temp_prifeesAmount = models.CharField(source='tempPrimaryFees.prifeesAmount')

    # secondary fees serializer
        temp_secfeesPaymentMethod = models.CharField(source='tempSecondaryFees.secfeesPaymentMethod')
        temp_secfeesBankName = models.CharField(source='tempSecondaryFees.secfeesBankName')
        temp_secfeesBankAccHolder = models.CharField(source='tempSecondaryFees.secfeesBankAccHolder')
        temp_secfeesBankAccCode = models.CharField(source='tempSecondaryFees.secfeesBankAccCode')
        temp_secfeesBranchCode = models.CharField(source='tempSecondaryFees.secfeesBranchCode')
        temp_secfeesBankAccNo = models.CharField(source='tempSecondaryFees.secfeesBankAccNo')
        temp_secfeesPayeeID = models.CharField(source='tempSecondaryFees.secfeesPayeeID')
        temp_secfeesApprovalDate = models.CharField(source='tempSecondaryFees.secfeesApprovalDate')
        temp_secfeesAttentionTo = models.CharField(source='tempSecondaryFees.secfeesAttentionTo')

    # refund serializer
        temp_refundPaymentMethod = models.CharField(source='tempRefund.refundPaymentMethod')
        temp_refundBankName = models.CharField(source='tempRefund.refundBankName')
        temp_refundBankAccHolder = models.CharField(source='tempRefund.refundBankAccHolder')
        temp_refundBankAccCode = models.CharField(source='tempRefund.refundBankAccCode')
        temp_refundBranchCode = models.CharField(source='tempRefund.refundBranchCode')
        temp_refundBankAccNo = models.CharField(source='tempRefund.refundBankAccNo')
        temp_refundApprovalReference = models.CharField(source='tempRefund.refundApprovalReference')
        temp_refundApprovalDate = models.CharField(source='tempRefund.refundApprovalDate')
        temp_refundDepositOpt = models.CharField(source='tempRefund.refundDepositOpt')

    # parent1 serializer
        temp_parent1Relationship = models.CharField(source='tempParent1.parent1Relationship')
        temp_parent1Name = models.CharField(source='tempParent1.parent1Name')
        temp_parent1Email = models.CharField(source='tempParent1.parent1Email')
        temp_parent1Mobile = models.CharField(source='tempParent1.parent1Mobile')
        temp_parent1Phone = models.CharField(source='tempParent1.parent1Phone')
        temp_parent1ID = models.CharField(source='tempParent1.parent1ID')
        temp_parent1Race = models.CharField(source='tempParent1.parent1Race')
        temp_parent1Citizenship = models.CharField(source='tempParent1.parent1Citizenship')
        temp_parent1Occupation = models.CharField(source='tempParent1.parent1Occupation')
        temp_parent1MainContact = models.CharField(source='tempParent1.parent1MainContact')
        temp_parent1AuthorisedPickUp = models.CharField(source='tempParent1.parent1AuthorisedPickUp')
        temp_parent1EmailInvoiceReceipt = models.CharField(source='tempParent1.parent1EmailInvoiceReceipt')
        temp_parent1EmailCheckIn = models.CharField(source='tempParent1.parent1EmailCheckIn')

    # parent2 serializer
        temp_parent2Relationship = models.CharField(source='tempParent2.parent2Relationship')
        temp_parent2Name = models.CharField(source='tempParent2.parent2Name')
        temp_parent2Email = models.CharField(source='tempParent2.parent2Email')
        temp_parent2Mobile = models.CharField(source='tempParent2.parent2Mobile')
        temp_parent2Phone = models.CharField(source='tempParent2.parent2Phone')
        temp_parent2ID = models.CharField(source='tempParent2.parent2ID')
        temp_parent2Race = models.CharField(source='tempParent2.parent2Race')
        temp_parent2Citizenship = models.CharField(source='tempParent2.parent2Citizenship')
        temp_parent2Occupation = models.CharField(source='tempParent2.parent2Occupation')
        temp_parent2MainContact = models.CharField(source='tempParent2.parent2MainContact')
        temp_parent2AuthorisedPickUp = models.CharField(source='tempParent2.parent2AuthorisedPickUp')
        temp_parent2EmailInvoiceReceipt = models.CharField(source='tempParent2.parent2EmailInvoiceReceipt')
        temp_parent2EmailCheckIn = models.CharField(source='tempParent2.parent2EmailCheckIn')

    # parent3 serializer
        temp_parent3Relationship = models.CharField(source='tempParent3.parent3Relationship')
        temp_parent3Name = models.CharField(source='tempParent3.parent3Name')
        temp_parent3Email = models.CharField(source='tempParent3.parent3Email')
        temp_parent3Mobile = models.CharField(source='tempParent3.parent3Mobile')
        temp_parent3Phone = models.CharField(source='tempParent3.parent3Phone')
        temp_parent3ID = models.CharField(source='tempParent3.parent3ID')
        temp_parent3Race = models.CharField(source='tempParent3.parent3Race')
        temp_parent3Citizenship = models.CharField(source='tempParent3.parent3Citizenship')
        temp_parent3Occupation = models.CharField(source='tempParent3.parent3Occupation')
        temp_parent3MainContact = models.CharField(source='tempParent3.parent3MainContact')
        temp_parent3AuthorisedPickUp = models.CharField(source='tempParent3.parent3AuthorisedPickUp')
        temp_parent3EmailInvoiceReceipt = models.CharField(source='tempParent3.parent3EmailInvoiceReceipt')
        temp_parent3EmailCheckIn = models.CharField(source='tempParent3.parent3EmailCheckIn')
    
    # motherAdd serializer
        temp_motherAddBlock = models.CharField(source='tempMotherAdd.motherAddBlock')
        temp_motherAddBuilding = models.CharField(source='tempMotherAdd.motherAddBuilding')
        temp_motherAddStreet = models.CharField(source='tempMotherAdd.motherAddStreet')
        temp_motherAddUnit = models.CharField(source='tempMotherAdd.motherAddUnit')
        temp_motherAddPostalCode = models.CharField(source='tempMotherAdd.motherAddPostalCode')
        temp_motherAddTransport = models.CharField(source='tempMotherAdd.motherAddTransport')

    # fatherAdd serializer
        temp_fatherAddBlock = models.CharField(source='tempFatherAdd.fatherAddBlock')
        temp_fatherAddBuilding = models.CharField(source='tempFatherAdd.fatherAddBuilding')
        temp_fatherAddStreet = models.CharField(source='tempFatherAdd.fatherAddStreet')
        temp_fatherAddUnit = models.CharField(source='tempFatherAdd.fatherAddUnit')
        temp_fatherAddPostalCode = models.CharField(source='tempFatherAdd.fatherAddPostalCode')
        temp_fatherAddTransport = models.CharField(source='tempFatherAdd.fatherAddTransport')

    # address serializer
        temp_address1Line1 = models.CharField(source='tempAddress.address1Line1')
        temp_address1Line2 = models.CharField(source='tempAddress.address1Line2')
        temp_address1PostalCode = models.CharField(source='tempAddress.address1PostalCode')
        temp_address1Transport = models.CharField(source='tempAddress.address1Transport')

    # emergency serializer
        temp_emergency1Relationship = models.CharField(source='tempEmergency.emergency1Relationship')
        temp_emergency1Name = models.CharField(source='tempEmergency.emergency1Name')
        temp_emergency1Mobile = models.CharField(source='tempEmergency.emergency1Mobile')
        temp_emergency1Phone = models.CharField(source='tempEmergency.emergency1Phone')
        temp_emergency1Email = models.CharField(source='tempEmergency.emergency1Email')

    class Meta:
        model = Temporary
        fields = '__all__'

class CoreServiceFamilySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = CoreServiceFamily
        fields = '__all__'

class CoreServiceChildrenMedicalContactSerializers(serializers.ModelSerializer):

    createdAt = serializers.DateTimeField(read_only=True)
    updatedAt = serializers.DateTimeField(read_only=True)

    class Meta:
        model = CoreServiceChildrenMedicalContact
        fields = '__all__'
