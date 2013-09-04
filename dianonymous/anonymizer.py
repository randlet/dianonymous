import dicom


ANONYMOUS_AGE = "200"
AGE_STRING = "AS"
PERSONS_NAME = "PN"

UPPER_BYTE_MASK = 0xFF00
UPPER_BYTE_OF_CURVE_GROUP = 0x5000


#       if data.has_key('rtss'):
#            self.updateElement(rtss, 'SeriesDescription', 'RT Structure Set')
#            self.updateElement(rtss, 'StructureSetDate', '19010101')
#            self.updateElement(rtss, 'StructureSetTime', '000000')
#            if rtss.has_key('RTROIObservations'):
#                for item in rtss.RTROIObservations:
#                    self.updateElement(item, 'ROIInterpreter', 'anonymous')
#            rtss.save_as(os.path.join(path, 'rtss.dcm'))
#
#        if data.has_key('rtplan'):
#            rtplan = data['rtplan']
#            wx.CallAfter(progressFunc, i, length,
#                'Anonymizing file ' + str(i) + ' of ' + str(length))
#            self.updateCommonElements(rtplan, name, patientid, privatetags)
#            self.updateElement(rtplan, 'SeriesDescription', 'RT Plan')
#            self.updateElement(rtplan, 'RTPlanName', 'plan')
#            self.updateElement(rtplan, 'RTPlanDate', '19010101')
#            self.updateElement(rtplan, 'RTPlanTime', '000000')
#            if rtplan.has_key('ToleranceTables'):
#                for item in rtplan.ToleranceTables:
#                    self.updateElement(item, 'ToleranceTableLabel', 'tolerance')
#            if rtplan.has_key('Beams'):
#                for item in rtplan.Beams:
#                    self.updateElement(item, 'Manufacturer', 'manufacturer')
#                    self.updateElement(item, 'InstitutionName', 'institution')
#                    self.updateElement(item, 'InstitutionAddress', 'address')
#                    self.updateElement(item, 'InstitutionalDepartmentName', 'department')
#                    self.updateElement(item, 'ManufacturersModelName', 'model')
#                    self.updateElement(item, 'TreatmentMachineName', 'txmachine')
#            if rtplan.has_key('TreatmentMachines'):
#                for item in rtplan.TreatmentMachines:
#                    self.updateElement(item, 'Manufacturer', 'manufacturer')
#                    self.updateElement(item, 'InstitutionName', 'vendor')
#                    self.updateElement(item, 'InstitutionAddress', 'address')
#                    self.updateElement(item, 'InstitutionalDepartmentName', 'department')
#                    self.updateElement(item, 'ManufacturersModelName', 'model')
#                    self.updateElement(item, 'DeviceSerialNumber', '0')
#                    self.updateElement(item, 'TreatmentMachineName', 'txmachine')
#            if rtplan.has_key('Sources'):
#                for item in rtplan.Sources:
#                    self.updateElement(item, 'SourceManufacturer', 'manufacturer')
#                    self.updateElement(item, 'SourceIsotopeName', 'isotope')
#            rtplan.save_as(os.path.join(path, 'rtplan.dcm'))
#            i = i + 1
#        if data.has_key('rtdose'):
#            rtdose = data['rtdose']
#            wx.CallAfter(progressFunc, i, length,
#                'Anonymizing file ' + str(i) + ' of ' + str(length))
#            self.updateCommonElements(rtdose, name, patientid, privatetags)
#            self.updateElement(rtdose, 'SeriesDescription', 'RT Dose')
#            rtdose.save_as(os.path.join(path, 'rtdose.dcm'))
#            i = i + 1
#        if data.has_key('images'):
#            images = data['images']
#            for n, image in enumerate(images):
#                wx.CallAfter(progressFunc, i, length,
#                    'Anonymizing file ' + str(i) + ' of ' + str(length))
#                self.updateCommonElements(image, name, patientid, privatetags)
#                self.updateElement(image, 'SeriesDate', '19010101')
#                self.updateElement(image, 'ContentDate', '19010101')
#                self.updateElement(image, 'SeriesTime', '000000')
#                self.updateElement(image, 'ContentTime', '000000')
#                self.updateElement(image, 'InstitutionName', 'institution')
#                self.updateElement(image, 'InstitutionAddress', 'address')
#                self.updateElement(image, 'InstitutionalDepartmentName', 'department')
#                modality = image.SOPClassUID.name.partition(' Image Storage')[0]
#                image.save_as(
#                    os.path.join(path, modality.lower() + '.' + str(n) + '.dcm'))
#                i = i + 1
#           self.updateElement(rtss, 'SeriesDescription', 'RT Structure Set')
#            self.updateElement(rtss, 'StructureSetDate', '19010101')
#            self.updateElement(rtss, 'StructureSetTime', '000000')
#
#            self.updateElement(rtplan, 'SeriesDescription', 'RT Plan')
#            self.updateElement(rtplan, 'RTPlanName', 'plan')
#            self.updateElement(rtplan, 'RTPlanDate', '19010101')
#            self.updateElement(rtplan, 'RTPlanTime', '000000')
#        self.updateElement(data, 'OtherPatientIDs', patientid)
#        self.updateElement(data, 'OtherPatientNames', name)
#        self.updateElement(data, 'InstanceCreationDate', '19010101')
#        self.updateElement(data, 'InstanceCreationTime', '000000')
#        self.updateElement(data, 'StudyDate', '19010101')
#        self.updateElement(data, 'StudyTime', '000000')
#        self.updateElement(data, 'AccessionNumber', '')
#        self.updateElement(data, 'Manufacturer', 'manufacturer')
#        self.updateElement(data, 'ReferringPhysiciansName', 'physician')
#        self.updateElement(data, 'StationName', 'station')
#        self.updateElement(data, 'NameofPhysiciansReadingStudy', 'physician')
#        self.updateElement(data, 'OperatorsName', 'operator')
#        self.updateElement(data, 'PhysiciansofRecord', 'physician')
#        self.updateElement(data, 'ManufacturersModelName', 'model')
#        self.updateElement(data, 'PatientsBirthDate', '')
#        self.updateElement(data, 'PatientsSex', 'O')
#        self.updateElement(data, 'PatientsAge', '000Y')
#        self.updateElement(data, 'PatientsWeight', 0)
#        self.updateElement(data, 'PatientsSize', 0)
#        self.updateElement(data, 'PatientsAddress', 'address')
#        self.updateElement(data, 'AdditionalPatientHistory', '')
#        self.updateElement(data, 'EthnicGroup', 'ethnicity')
#        self.updateElement(data, 'StudyID', '1')
#        self.updateElement(data, 'DeviceSerialNumber', '0')
#        self.updateElement(data, 'SoftwareVersions', '1.0')
#        self.updateElement(data, 'ReviewDate', '19010101')
#        self.updateElement(data, 'ReviewTime', '000000')
#        self.updateElement(data, 'ReviewerName', 'anonymous')

TAGS_TO_ANONYMIZE = {
    (0x0008, 0x0014): {"name": "InstanceCreatorUID", "method": None},
    (0x0008, 0x0018): {"name": "SOPInstanceUID", "method": None},
    (0x0008, 0x0050): {"name": "AccessionNumber", "method": None},
    (0x0008, 0x0080): {"name": "InstitutionName", "method": None},
    (0x0008, 0x0081): {"name": "InstitutionAddress", "method": None},
    (0x0008, 0x0090): {"name": "ReferringPhysiciansName", "method": None},
    (0x0008, 0x0092): {"name": "ReferringPhysiciansAddress", "method": None},
    (0x0008, 0x0094): {"name": "ReferringPhysiciansTelephoneNumber", "method": None},
    (0x0008, 0x1010): {"name": "StationName", "method": None},
    (0x0008, 0x1030): {"name": "StudyDescription", "method": None},
    (0x0008, 0x103E): {"name": "SeriesDescription", "method": None},
    (0x0008, 0x1040): {"name": "InstitutionalDepartmentName", "method": None},
    (0x0008, 0x1048): {"name": "PhysiciansofRecord", "method": None},
    (0x0008, 0x1050): {"name": "PerformingPhysiciansName", "method": None},
    (0x0008, 0x1060): {"name": "NameofPhysiciansReadingStudy", "method": None},
    (0x0008, 0x1070): {"name": "OperatorsName", "method": None},
    (0x0008, 0x1080): {"name": "AdmittingDiagnosesDescription", "method": None},
    (0x0008, 0x1155): {"name": "ReferencedSOPInstanceUID", "method": None},
    (0x0008, 0x2111): {"name": "DerivationDescription", "method": None},
    (0x0010, 0x0010): {"name": "PatientsName", "method": None},
    (0x0010, 0x0020): {"name": "PatientID", "method": None},
    (0x0010, 0x0030): {"name": "PatientsBirthDate", "method": None},
    (0x0010, 0x0032): {"name": "PatientsBirthTime", "method": None},
    (0x0010, 0x0040): {"name": "PatientsSex", "method": None},
    (0x0010, 0x1000): {"name": "OtherPatientIds", "method": None},
    (0x0010, 0x1001): {"name": "OtherPatientNames", "method": None},
    (0x0010, 0x1010): {"name": "PatientsAge", "method": None},
    (0x0010, 0x1020): {"name": "PatientsSize", "method": None},
    (0x0010, 0x1030): {"name": "PatientsWeight", "method": None},
    (0x0010, 0x1030): {"name": "PatientsAddress", "method": None},
    (0x0010, 0x1090): {"name": "MedicalRecordLocator", "method": None},
    (0x0010, 0x2160): {"name": "EthnicGroup", "method": None},
    (0x0010, 0x2180): {"name": "Occupation", "method": None},
    (0x0010, 0x21B0): {"name": "AdditionalPatientsHistory", "method": None},
    (0x0010, 0x4000): {"name": "PatientComments", "method": None},
    (0x0018, 0x1000): {"name": "DeviceSerialNumber", "method": None},
    (0x0018, 0x1030): {"name": "ProtocolName", "method": None},
    (0x0020, 0x000D): {"name": "StudyInstanceUID", "method": None},
    (0x0020, 0x000E): {"name": "SeriesInstanceUID", "method": None},
    (0x0020, 0x0010): {"name": "StudyID", "method": None},
    (0x0020, 0x0052): {"name": "FrameofReferenceUID", "method": None},
    (0x0020, 0x0200): {"name": "SynchronizationFrameofReferenceUID", "method": None},
    (0x0020, 0x4000): {"name": "ImageComments", "method": None},
    (0x0040, 0x0275): {"name": "RequestAttributesSequence", "method": None},
    (0x0040, 0xA124): {"name": "UID", "method": None},
    (0x0040, 0xA730): {"name": "ContentSequence", "method": None},
    (0x0088, 0x0140): {"name": "StorageMediaFile-setUID", "method": None},
    (0x3006, 0x0024): {"name": "ReferencedFrameofReferenceUID ", "method": None},
    (0x3006, 0x00C2): {"name": "RelatedFrameofReferenceUID", "method": None},
}
SET_OF_TAGS_TO_ANONYMIZE = set(TAGS_TO_ANONYMIZE.keys())

# AE : Application Name
# AS : Age String: nnnW or nnnM or nnnY
# AT : Attribute Tag gggg,eeee
# CS : Code String
# DA : Date yyyymmdd (check for yyyy.mm.dd also and convert)
# DS : Decimal String may start with + or - and may be padded with l or t space
# DT : Date Time YYYYMMDDHHMMSS.FFFFFF&ZZZZ (&ZZZ is optional & = + or -)
# FL : Single precision floating pt number (float)
# FD : Double precision floating pt number (double)
# IS : Integer encoded as string. may be padded
# LO : Character string. can be padded. cannot contain \ or any control chars except ESC
# LT : Long Text. Leading spaces are significant. trailing spaces arent
# OB : single trailing 0x00 to make even number of bytes. Transfer Syntax determines len
# OF : Other Float String. floats
# OW : Other Word String. words
# PN : Person's Name 64byte max per component. 5 components. delimiter = ^
# SH : Short String. may be padded
# SL : signed long integer
# SQ : Sequence of zero or more items
# SS : signed short integer (word)
# ST : Short Text of chars
# TM : Time hhmmss.frac (or older format: hh:mm:ss.frac)
# UI : Unique Identifier (delimiter = .) 0-9 only, trailing space to make even #
# UL : Unsigned long integer
# UN : unknown
# US : Unsigned short integer (word)
# UT : Unlimited Text. trailing spaces ignored

def convert_string(ds, elem):
    return elem.value

DEFAULT_METHODS = {
    "AE" : convert_string,
    "AS" : convert_string,
    "AT" : convert_string,
    "CS" : convert_string,
    "DA" : convert_string,
    "DS" : convert_string,
    "DT" : convert_string,
    "FL" : convert_string,
    "FD" : convert_string,
    "IS" : convert_string,
    "LO" : convert_string,
    "LT" : convert_string,
    "OB" : convert_string,
    "OF" : convert_string,
    "OW" : convert_string,
    "PN" : convert_string,
    "SH" : convert_string,
    "SL" : convert_string,
    "SQ" : convert_string,
    "SS" : convert_string,
    "ST" : convert_string,
    "TM" : convert_string,
    "UI" : convert_string,
    "UL" : convert_string,
    "UN" : convert_string,
    "US" : convert_string,
    "UT" : convert_string,
}

def anonymize(dcm, patient_id="pid", patient_name="anonymous", private=True ):
    """return an anonymized version of input dcm file object """

    # Define call-back functions for the dcm.walk() function
    def callback(ds, data_element):
        """Called from the dcm "walk" recursive function for all data elements."""

        t = data_element.tag
        if private and t.is_private:
            del ds[t]
        elif (t.group, t.elem) in SET_OF_TAGS_TO_ANONYMIZE:
            fun = TAGS_TO_ANONYMIZE[(t.group, t.elem)]["method"]
            if fun is None:
                fun = DEFAULT_METHODS[data_element.VR]
            data_element.value = fun(ds, data_element)
        elif t.group & UPPER_BYTE_MASK == UPPER_BYTE_OF_CURVE_GROUP:
            del ds[t]

    dcm.walk(callback)
