# ARMC Imaging MVP â€” Integration Test Results



## Project Information



Project: Akech Rose Medical Center (ARMC)

Environment: Local synthetic development lab



Integration Components:

\- NextGen Mirth Connect

\- HL7 v2 ORM messages

\- JavaScript

\- Orthanc PACS

\- DICOM

\- Orthanc REST API



## Test 1 â€” Positive Accession Lookup



Test ID: M10F-POS-001



HL7 Message Control ID: ARMC-ORM-0008



Mirth Message ID: 9



Accession Number: ARMC-ACC-1001



Objective:

Verify that an HL7 ORM message can trigger a successful

lookup of an existing DICOM imaging study.



Expected Result:

The Orthanc lookup returns one matching study.



Actual Result:

The lookup successfully returned the existing Orthanc study.



Orthanc Study ID:

2d59759b-ca394b5f-1554f945-a59f5098-70c9cbb5



Mirth Destination Status: SENT



Processing Errors: None observed for message 9.



Result: PASS



## Test 2 â€” Negative Accession Lookup



Test ID: M10E-NEG-001



HL7 Message Control ID: ARMC-ORM-0007



Mirth Message ID: 8



Accession Number: ARMC-ACC-NOTFOUND-9999



Objective:

Verify that an HL7 ORM message containing an unknown

accession number is handled without a processing error.



Expected Result:

The Orthanc lookup returns a controlled NOT_FOUND response.



Actual Result:

ARMC M10E: NOT_FOUND - No Orthanc study for accession

ARMC-ACC-NOTFOUND-9999



Mirth Destination Status: SENT



Processing Errors: None observed for message 8.



Result: PASS



## Regression Test Summary



Positive lookup: PASS



Negative lookup: PASS



Overall functional regression result: PASS



## Evidence



Positive test:

../evidence/ARMC_M10F_Positive_Regression_PASSED.png



Negative test:

../evidence/ARMC_M10E_Negative_Lookup_PASSED.png



## Limitations



All patient information and imaging data are synthetic.



Testing was performed in a local development environment.



This MVP demonstrates accession-based retrieval of

an existing Orthanc imaging study.



It does not establish production EHR/PACS integration,

automated DICOM image creation from HL7 orders,

or complete radiology workflow management.
