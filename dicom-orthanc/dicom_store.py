import pydicom
from pynetdicom import AE

filename = "/workspace/synthetic-dicom/ARMC_Synthetic_Image_001.dcm"

# Read synthetic DICOM image
ds = pydicom.dcmread(filename)

# Configure DICOM client
ae = AE(ae_title="ARMC_TEST")

# Request the image's storage SOP class and transfer syntax
ae.add_requested_context(
    ds.SOPClassUID,
    ds.file_meta.TransferSyntaxUID
)

# Establish DICOM association
assoc = ae.associate(
    "armc-orthanc",
    4242,
    ae_title="ARMC_PACS"
)

if assoc.is_established:
    print("DICOM association established")

    status = assoc.send_c_store(ds)

    if status and status.Status == 0x0000:
        print("SUCCESS: DICOM C-STORE completed")
        print("Patient ID:", ds.PatientID)
        print("Study UID:", ds.StudyInstanceUID)
        print("SOP Instance UID:", ds.SOPInstanceUID)
        print("Status: 0x0000")
    else:
        print("FAILED: DICOM C-STORE unsuccessful")
        if status:
            print("Status:", hex(status.Status))

    assoc.release()
else:
    print("FAILED: DICOM association not established")
