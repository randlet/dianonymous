import dicom
import uuid
import hashlib


ANONYMOUS_AGE = "200"
AGE_STRING = "AS"
PERSONS_NAME = "PN"

UPPER_BYTE_MASK = 0xFF00
UPPER_BYTE_OF_CURVE_GROUP = 0x5000

def anonymous_id(ds, elem):
    return "1234567890"

def anonymous_study_id(ds, elem):
    return "1"

def anonymous_uid(ds, elem):
    return uuid.UUID(hashlib.sha512(str(elem.tag)).hexdigest()[:32]).get_hex()

def anonymous_string(ds, elem):
    return "anonymous"

def anonymous_date(ds, elem):
    return "19010101"

def anonymous_datetime(ds, elem):
    return "19010101000000.000000"

def anonymous_time(ds, elem):
    return "000000.000"

def anonymous_number(ds, elem):
    return 0

def anonymous_sex(ds, elem):
    return ""

def anonymous_decimal_string(ds, elem):
    return "0.000"

def anonymous_integer_string(ds, elem):
    return "0"

def no_change(ds, elem):
    return elem.value


DEFAULT_METHODS = {
    "AE" : no_change,
    "AS" : anonymous_string,
    "AT" : no_change,
    "CS" : no_change,
    "DA" : anonymous_date,
    "DS" : no_change,
    "DT" : anonymous_datetime,
    "FL" : no_change,
    "FD" : no_change,
    "IS" : no_change,
    "LO" : no_change,
    "LT" : no_change,
    "OB" : no_change,
    "OF" : no_change,
    "OW" : no_change,
    "PN" : anonymous_string,
    "SH" : no_change,
    "SL" : no_change,
    "SQ" : no_change,
    "SS" : no_change,
    "ST" : no_change,
    "TM" : anonymous_string,
    "UI" : no_change,
    "UL" : no_change,
    "UN" : no_change,
    "US" : no_change,
    "UT" : no_change,
}


TAGS_TO_ANONYMIZE = {
    (0x0008, 0x0014): {"name": "InstanceCreatorUID", "method": anonymous_uid},
    (0x0008, 0x0018): {"name": "SOPInstanceUID", "method": anonymous_uid},
    (0x0008, 0x0050): {"name": "AccessionNumber", "method": None},
    (0x0008, 0x0080): {"name": "InstitutionName", "method": anonymous_string},
    (0x0008, 0x0081): {"name": "InstitutionAddress", "method": anonymous_string},
    (0x0008, 0x0090): {"name": "ReferringPhysiciansName", "method": anonymous_string},
    (0x0008, 0x0092): {"name": "ReferringPhysiciansAddress", "method": anonymous_string},
    (0x0008, 0x0094): {"name": "ReferringPhysiciansTelephoneNumber", "method": anonymous_string},
    (0x0008, 0x1010): {"name": "StationName", "method": anonymous_string},
    (0x0008, 0x1030): {"name": "StudyDescription", "method": anonymous_string},
    (0x0008, 0x103E): {"name": "SeriesDescription", "method": anonymous_string},
    (0x0008, 0x1040): {"name": "InstitutionalDepartmentName", "method": anonymous_string},
    (0x0008, 0x1048): {"name": "PhysiciansofRecord", "method": anonymous_string},
    (0x0008, 0x1050): {"name": "PerformingPhysiciansName", "method": anonymous_string},
    (0x0008, 0x1060): {"name": "NameofPhysiciansReadingStudy", "method": anonymous_string},
    (0x0008, 0x1070): {"name": "OperatorsName", "method": anonymous_string},
    (0x0008, 0x1080): {"name": "AdmittingDiagnosesDescription", "method": None},
    (0x0008, 0x1155): {"name": "ReferencedSOPInstanceUID", "method": anonymous_uid},
    (0x0008, 0x2111): {"name": "DerivationDescription", "method": None},
    (0x0010, 0x0010): {"name": "PatientsName", "method": anonymous_string},
    (0x0010, 0x0020): {"name": "PatientID", "method": anonymous_id},
    (0x0010, 0x0030): {"name": "PatientsBirthDate", "method": anonymous_date},
    (0x0010, 0x0032): {"name": "PatientsBirthTime", "method": anonymous_time},
    (0x0010, 0x0040): {"name": "PatientsSex", "method": anonymous_sex},
    (0x0010, 0x1000): {"name": "OtherPatientIds", "method": anonymous_string},
    (0x0010, 0x1001): {"name": "OtherPatientNames", "method": anonymous_string},
    (0x0010, 0x1010): {"name": "PatientsAge", "method": anonymous_integer_string},
    (0x0010, 0x1020): {"name": "PatientsSize", "method": anonymous_number},
    (0x0010, 0x1030): {"name": "PatientsWeight", "method": anonymous_decimal_string},
    (0x0010, 0x1040): {"name": "PatientsAddress", "method": anonymous_string},
    (0x0010, 0x1090): {"name": "MedicalRecordLocator", "method": None},
    (0x0010, 0x2160): {"name": "EthnicGroup", "method": anonymous_string},
    (0x0010, 0x2180): {"name": "Occupation", "method": anonymous_string},
    (0x0010, 0x21B0): {"name": "AdditionalPatientsHistory", "method": anonymous_string},
    (0x0010, 0x4000): {"name": "PatientComments", "method": anonymous_string},
    (0x0018, 0x1000): {"name": "DeviceSerialNumber", "method": anonymous_string},
    (0x0018, 0x1030): {"name": "ProtocolName", "method": anonymous_string},
    (0x0020, 0x000D): {"name": "StudyInstanceUID", "method": anonymous_uid},
    (0x0020, 0x000E): {"name": "SeriesInstanceUID", "method": anonymous_uid},
    (0x0020, 0x0010): {"name": "StudyID", "method": anonymous_study_id},
    (0x0020, 0x0052): {"name": "FrameofReferenceUID", "method": anonymous_uid},
    (0x0020, 0x0200): {"name": "SynchronizationFrameofReferenceUID", "method": anonymous_uid},
    (0x0020, 0x4000): {"name": "ImageComments", "method": anonymous_string},
    (0x0040, 0x0275): {"name": "RequestAttributesSequence", "method": None},
    (0x0040, 0xA124): {"name": "UID", "method": anonymous_uid},
    (0x0040, 0xA730): {"name": "ContentSequence", "method": None},
    (0x0088, 0x0140): {"name": "StorageMediaFile-setUID", "method": anonymous_uid},
    (0x3006, 0x0024): {"name": "ReferencedFrameofReferenceUID ", "method": anonymous_uid},
    (0x3006, 0x00C2): {"name": "RelatedFrameofReferenceUID", "method": anonymous_uid},
}


SET_OF_TAGS_TO_ANONYMIZE = set(TAGS_TO_ANONYMIZE.keys())

def anonymize(dcm, patient_id=None, patient_name=None, private=True ):
    """return an anonymized version of input dcm file object """

    # Define call-back functions for the dcm.walk() function
    def callback(ds, data_element):
        """Called from the dcm "walk" recursive function for all data elements."""

        t = data_element.tag
        hext = (t.group, t.elem)

        if patient_name is not None and hext in ((0x0010, 0x0010), (0x0010, 0x1001),):
            data_element.value = patient_name
        elif patient_id is not None and hext in ((0x0010, 0x1000), (0x0010, 0x0020),):
            data_element.value = patient_id
        elif private and t.is_private:
            del ds[t]
        elif hext in SET_OF_TAGS_TO_ANONYMIZE:
            fun = TAGS_TO_ANONYMIZE[hext]["method"]
            if fun is None:
                fun = DEFAULT_METHODS[data_element.VR]
            try:
                data_element.value = fun(ds, data_element)
            except ValueError:
                raise ValueError("Unable to convert data_element (%s, %s) with function %s" % (data_element.tag, data_element.name, fun))
        elif t.group & UPPER_BYTE_MASK == UPPER_BYTE_OF_CURVE_GROUP:
            del ds[t]


    dcm.walk(callback)
