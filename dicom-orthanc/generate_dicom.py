from datetime import datetime


import pydicom
from pydicom.dataset import FileDataset, FileMetaDataset
from pydicom.uid import (
    ExplicitVRLittleEndian,
    SecondaryCaptureImageStorage,
    generate_uid,
)

filename = "/workspace/synthetic-dicom/ARMC_Synthetic_Image_001.dcm"

# Generate synthetic grayscale image
pixels = bytes((x + y) % 256 for y in range(256) for x in range(256))


file_meta = FileMetaDataset()
file_meta.MediaStorageSOPClassUID = SecondaryCaptureImageStorage
file_meta.MediaStorageSOPInstanceUID = generate_uid()
file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
file_meta.ImplementationClassUID = generate_uid()

ds = FileDataset(filename, {}, file_meta=file_meta, preamble=b"\0" * 128)

now = datetime.now()

ds.PatientName = "ARMC^TestPatient"
ds.PatientID = "ARMC-DICOM-001"
ds.PatientBirthDate = "19900101"
ds.PatientSex = "O"

ds.StudyInstanceUID = generate_uid()
ds.SeriesInstanceUID = generate_uid()
ds.SOPClassUID = SecondaryCaptureImageStorage
ds.SOPInstanceUID = file_meta.MediaStorageSOPInstanceUID

ds.StudyDate = now.strftime("%Y%m%d")
ds.StudyTime = now.strftime("%H%M%S")
ds.ContentDate = ds.StudyDate
ds.ContentTime = ds.StudyTime

ds.Modality = "OT"
ds.StudyDescription = "ARMC Synthetic Imaging Test"
ds.SeriesNumber = 1
ds.InstanceNumber = 1
ds.ConversionType = "SYN"
ds.ImageType = ["DERIVED", "SECONDARY"]

ds.Rows = 256
ds.Columns = 256
ds.SamplesPerPixel = 1
ds.PhotometricInterpretation = "MONOCHROME2"
ds.BitsAllocated = 8
ds.BitsStored = 8
ds.HighBit = 7
ds.PixelRepresentation = 0
ds.PixelData = pixels

ds.save_as(filename, enforce_file_format=True)

print("DICOM file created:", filename)
print("Patient ID:", ds.PatientID)
print("Modality:", ds.Modality)
print("Study UID:", ds.StudyInstanceUID)
