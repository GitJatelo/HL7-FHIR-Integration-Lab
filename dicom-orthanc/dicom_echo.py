from pynetdicom import AE
from pynetdicom.sop_class import Verification

ae = AE(ae_title="ARMC_TEST")
ae.add_requested_context(Verification)

assoc = ae.associate(
    "armc-orthanc",
    4242,
    ae_title="ARMC_PACS"
)

if assoc.is_established:
    status = assoc.send_c_echo()

    if status and status.Status == 0x0000:
        print("SUCCESS: DICOM C-ECHO verified")
        print("PACS: ARMC_PACS")
        print("Port: 4242")
        print("Status: 0x0000")
    else:
        print("FAILED: C-ECHO response unsuccessful")

    assoc.release()
else:
    print("FAILED: DICOM association not established")
