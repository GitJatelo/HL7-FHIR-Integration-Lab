\# ARMC Imaging Integration MVP



\## Project Overview



Project: Akech Rose Medical Center (ARMC)



Environment: Local synthetic healthcare interoperability lab



Technologies:

\- HL7 v2 ORM messages

\- NextGen Mirth Connect

\- JavaScript

\- Orthanc PACS

\- DICOM

\- REST APIs

\- Docker

\- PowerShell



\## 1. Project Objective



Demonstrate how an HL7 ORM imaging order can be processed

through Mirth Connect and used to locate an existing imaging

study in Orthanc PACS.



All patient and imaging data are synthetic.



\## 2. Verified Architecture



Synthetic HL7 ORM Message

&#x20;         |

&#x20;         v

Mirth Connect TCP Listener

127.0.0.1:6661

&#x20;         |

&#x20;         v

Mirth Source Transformer

Extract imaging accession number from OBR-18

&#x20;         |

&#x20;         v

Orthanc\_Study\_Lookup

JavaScript Writer

&#x20;         |

&#x20;         v

Orthanc REST API

127.0.0.1:8042

&#x20;         |

&#x20;         v

Search for matching DICOM study

&#x20;         |

&#x20;         v

Return matching study ID or NOT\_FOUND



\## 3. Positive Integration Test



Message Control ID: ARMC-ORM-0008



Accession Number: ARMC-ACC-1001



Expected Result:

One matching Orthanc imaging study.



Actual Result:

Lookup successful.



Orthanc Study ID:

2d59759b-ca394b5f-1554f945-a59f5098-70c9cbb5



Mirth Destination Status: SENT



Result: PASS



\## 4. Negative Integration Test



Message Control ID: ARMC-ORM-0007



Accession Number:

ARMC-ACC-NOTFOUND-9999



Expected Result:

No matching Orthanc study.



Actual Result:

NOT\_FOUND returned without a destination processing error.



Result: PASS



\## 5. Evidence



Positive regression screenshot:

evidence/ARMC\_M10F\_Positive\_Regression\_PASSED.png



Validated channel backup:

ARMC\_HL7\_ORM\_IMAGING\_DEV\_M10E\_Validated\_Backup.xml



\## 6. Current Limitations



This MVP uses synthetic healthcare data.



The workflow demonstrates accession-based lookup

of an existing DICOM study.



It does not yet demonstrate:

\- Automatic DICOM image creation from an HL7 order

\- Production EHR integration

\- Production PACS integration

\- Full radiology workflow management



\## 7. Project Status



M10E: COMPLETE

M10F: COMPLETE

M10G: Documentation in progress



\## 8. Next Development Opportunities



\- HL7 ORM order validation

\- Improved negative and duplicate-study handling

\- Structured integration logging

\- Automated regression testing

\- Healthcare interoperability portfolio demonstration
