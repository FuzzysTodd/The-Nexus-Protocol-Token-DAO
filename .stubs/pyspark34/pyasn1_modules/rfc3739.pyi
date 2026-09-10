from _typeshed import Incomplete
from pyasn1.type import char, univ, useful
from pyasn1_modules import rfc5280 as rfc5280

MAX: Incomplete
qcStatementMap: Incomplete
AlgorithmIdentifier = rfc5280.AlgorithmIdentifier
AttributeType = rfc5280.AttributeType
DirectoryString = rfc5280.DirectoryString
GeneralName = rfc5280.GeneralName
id_pkix: Incomplete
id_pe: Incomplete
id_pda: Incomplete
id_qcs: Incomplete
id_pda_dateOfBirth: Incomplete

class DateOfBirth(useful.GeneralizedTime): ...

id_pda_placeOfBirth: Incomplete

class PlaceOfBirth(DirectoryString): ...

id_pda_gender: Incomplete

class Gender(char.PrintableString):
    subtypeSpec: Incomplete

id_pda_countryOfCitizenship: Incomplete

class CountryOfCitizenship(char.PrintableString):
    subtypeSpec: Incomplete

id_pda_countryOfResidence: Incomplete

class CountryOfResidence(char.PrintableString):
    subtypeSpec: Incomplete

id_pe_biometricInfo: Incomplete

class PredefinedBiometricType(univ.Integer):
    namedValues: Incomplete
    subtypeSpec: Incomplete

class TypeOfBiometricData(univ.Choice):
    componentType: Incomplete

class BiometricData(univ.Sequence):
    componentType: Incomplete

class BiometricSyntax(univ.SequenceOf):
    componentType: Incomplete

id_pe_qcStatements: Incomplete

class NameRegistrationAuthorities(univ.SequenceOf):
    componentType: Incomplete
    subtypeSpec: Incomplete

class QCStatement(univ.Sequence):
    componentType: Incomplete

class QCStatements(univ.SequenceOf):
    componentType: Incomplete

class SemanticsInformation(univ.Sequence):
    componentType: Incomplete
    subtypeSpec: Incomplete

id_qcs_pkixQCSyntax_v1: Incomplete
id_qcs_pkixQCSyntax_v2: Incomplete
