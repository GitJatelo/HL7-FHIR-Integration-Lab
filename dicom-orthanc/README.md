# ARMC DICOM/PACS Interoperability Lab

## Project Overview

This project demonstrates a local DICOM imaging workflow using Orthanc PACS, Docker, Python, pydicom, and pynetdicom.

It is part of the Akech Rose Medical Center (ARMC) healthcare interoperability portfolio.

All imaging data used in this lab is synthetic.

## Technology Stack

- Orthanc PACS
- Docker and Docker Compose
- Python 3.12
- pydicom 3.0.1
- pynetdicom 3.0.4
- DICOM networking protocols
- Windows PowerShell

## Architecture

Synthetic DICOM Generator
        |
        v
Python DICOM Client
        |
        | C-ECHO / C-STORE
        v
Orthanc PACS
        |
        | Study Storage
        v
Orthanc Web Interface
        |
        | Study Export
        v
Retrieved DICOM Files
        |
        v
Metadata and Pixel Data Verification

## Verified Accomplishments

### 1. Orthanc PACS Deployment

Deployed Orthanc using Docker Compose.

Configured:
- DICOM AE Title: ARMC_PACS
- DICOM Port: 4242
- HTTP Port: 8042
- Persistent Docker storage
- Localhost-bound host ports

### 2. DICOM Connectivity

Successfully executed DICOM C-ECHO.

Result:
- Association established
- C-ECHO response: 0x0000
- Connectivity verified

### 3. Synthetic DICOM Generation

Generated a synthetic DICOM image.

Test characteristics:
- Patient ID: ARMC-DICOM-001
- Modality: OT
- Image dimensions: 256 x 256
- Transfer Syntax: Explicit VR Little Endian

### 4. DICOM C-STORE

Successfully transmitted the synthetic DICOM image to Orthanc.

Result:
- DICOM association established
- C-STORE status: 0x0000
- Study visible in Orthanc

### 5. DICOM Retrieval and Integrity

Exported the stored study from Orthanc.

Verified:
- Patient ID matched
- Study Instance UID matched
- Series Instance UID matched
- SOP Instance UID matched
- Pixel Data matched
- Pixel Data SHA-256 hashes matched

The exported DICOM file was not byte-for-byte identical
to the original, but its verified identifiers and pixel
data remained consistent.

## Project Files

- compose.yaml: Orthanc Docker configuration
- Dockerfile.dicom: Python DICOM tools image
- generate_dicom.py: Synthetic DICOM generation
- dicom_echo.py: DICOM C-ECHO connectivity test
- dicom_store.py: DICOM C-STORE transmission
- .gitignore: Excludes generated images and local data

## Security Considerations

This project is intended for local development.

- Docker host ports are bound to localhost.
- Synthetic imaging data is used.
- Generated and retrieved DICOM files are excluded from Git.
- The lab is not configured for production use.
- Authentication and TLS would be required before broader deployment.

## Future Development

- DICOM C-FIND study queries
- DICOM C-MOVE retrieval workflows
- DICOMweb exploration
- HL7 ORM imaging order integration
- FHIR ImagingStudy resource mapping
- Healthcare imaging security controls

## Project Status

Core DICOM storage and retrieval workflow: VERIFIED

Advanced interoperability integration: PLANNED
