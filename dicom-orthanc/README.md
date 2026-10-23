# ARMC DICOM/PACS Interoperability Lab

**Akech Rose Medical Center (ARMC)**

**Healthcare Interoperability Portfolio**

**Project Status:** Core DICOM/PACS workflow verified | HL7 ORM accession lookup verified | Advanced radiology integration planned

---

## 1. Project Overview

This project demonstrates a local healthcare imaging interoperability workflow using **Orthanc PACS, Docker, Python, pydicom, pynetdicom, HL7 v2, and Mirth Connect**.

The lab is part of the Akech Rose Medical Center (ARMC) healthcare interoperability portfolio.

It demonstrates two complementary capabilities:

1\. **DICOM/PACS integration:** Generating, transmitting, storing, retrieving, and validating synthetic medical imaging data.

2\. **HL7 ORM integration:** Processing synthetic imaging orders through Mirth Connect and querying Orthanc for existing studies using accession numbers.

**All patient and imaging data used in this lab is synthetic.**

The project is intended for learning, technical validation, and portfolio demonstration—not production clinical use.

---

## 2. Technology Stack

| Technology              | Purpose                               |

| ----------------------- | ------------------------------------- |

| Orthanc PACS 1.13.0     | DICOM study storage and REST API      |

| Docker / Docker Compose | Containerized infrastructure          |

| Python 3.12             | DICOM generation and testing          |

| pydicom 3.0.1           | DICOM dataset creation and inspection |

| pynetdicom 3.0.4        | DICOM networking                      |

| Mirth Connect 4.4.0     | HL7 interface processing              |

| HL7 v2 ORM^O01          | Synthetic imaging order messages      |

| Orthanc REST API        | Accession-based study lookup          |

| Windows PowerShell      | Local administration and validation   |

---

## 3. System Architecture

### 3.1 DICOM Storage and Retrieval

```text
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
```
### 3.2 HL7 ORM Imaging Order Integration

```text
Synthetic HL7 ORM^O01 Order
             |
             v
Mirth Connect TCP Listener
         Port 6661
             |
             v
HL7 Source Transformer
  Extract OBR-18 Accession
             |
             v
Orthanc REST API
  POST /tools/find
       Port 8042
             |
             v
Study Lookup by Accession
             |
       +-----+-----+
       |           |
       v           v
  MATCH FOUND    NO MATCH
       |           |
       v           v
 Return Study ID  Return NOT_FOUND
```

The HL7 integration queries existing Orthanc studies. It does not automatically create a DICOM study.

---

## 4. Verified DICOM/PACS Accomplishments

### 4.1 Orthanc PACS Deployment

Successfully deployed Orthanc using Docker Compose.

**Configuration:**

| Setting          | Value                      |

| ---------------- | -------------------------- |

| DICOM AE Title   | `ARMC\_PACS`                |

| DICOM Port       | `4242`                     |

| HTTP Port        | `8042`                     |

| Storage          | Persistent Docker storage  |

| Network exposure | Localhost-bound host ports |

**Result:** Orthanc deployment verified.

### 4.2 DICOM Connectivity

Successfully executed a DICOM C-ECHO operation.

**Results:**

* DICOM association established.

* C-ECHO response: `0x0000`.

* Connectivity verified.

### 4.3 Synthetic DICOM Generation

Generated a synthetic DICOM image with the following characteristics:

| Attribute        | Value                     |

| ---------------- | ------------------------- |

| Patient ID       | `ARMC-DICOM-001`          |

| Modality         | `OT`                      |

| Image dimensions | 256 × 256 |

| Transfer Syntax  | Explicit VR Little Endian |

### 4.4 DICOM C-STORE

Successfully transmitted the synthetic DICOM image to Orthanc.

**Results:**

* DICOM association established.

* C-STORE response: `0x0000`.

* Study visible in Orthanc.

### 4.5 DICOM Retrieval and Integrity

Successfully exported the stored DICOM study from Orthanc.

**Verified attributes:**

* Patient ID

* Study Instance UID

* Series Instance UID

* SOP Instance UID

* Pixel Data

* Pixel Data SHA-256 hash

**Finding:** Although the exported DICOM file was not byte-for-byte identical to the original, its verified identifiers and pixel data remained consistent.

---

## 5. HL7 ORM Imaging Order Integration — Verified

Extended the ARMC imaging lab with an HL7 v2 `ORM^O01` workflow using **Mirth Connect 4.4.0** and **Orthanc PACS 1.13.0**.

### 5.1 Integration Workflow

1\. Mirth Connect receives a synthetic HL7 ORM imaging order through TCP port `6661`.

2\. The source transformer extracts the accession number from `OBR-18`.

3\. A JavaScript Writer queries Orthanc through `POST /tools/find`.

4\. Orthanc searches for an existing study matching the accession number.

5\. The destination returns the matching study ID or a controlled `NOT_FOUND` response.

### 5.2 Verified Integration Tests

| Test | Scenario                 | Expected Result                                        | Status |

| ---- | ------------------------ | ------------------------------------------------------ | ------ |

| M10D | Dynamic accession lookup | Return matching Orthanc Study ID                       | PASS   |

| M10E | Unknown accession lookup | Controlled `NOT_FOUND` response                        | PASS   |

| M10F | Positive regression      | Confirm successful lookup after error-handling changes | PASS   |

**M10D — Dynamic Orthanc Lookup**

Successfully matched accession `ARMC-ACC-1001` to an existing synthetic Orthanc study.

**M10E — Negative Accession Lookup**

Confirmed that an unknown accession number produces a controlled `NOT_FOUND` response without a destination processing error.

**M10F — Positive Regression Test**

Repeated the successful accession lookup after implementing negative-case handling.

### 5.3 Supporting Documentation

- [ARMC Imaging MVP Architecture](../docs/ARMC_Imaging_MVP_Architecture.md)
- [ARMC Imaging MVP Test Results](../docs/ARMC_Imaging_MVP_Test_Results.md)

---

## 6. Project Files

| File                | Description                                     |

| ------------------- | ----------------------------------------------- |

| `compose.yaml`      | Orthanc Docker configuration                    |

| `Dockerfile.dicom`  | Python DICOM tools container                    |

| `generate\_dicom.py` | Synthetic DICOM generation                      |

| `dicom\_echo.py`     | DICOM C-ECHO connectivity testing               |

| `dicom\_store.py`    | DICOM C-STORE transmission                      |

| `.gitignore`        | Excludes generated data and local configuration |

| `README.md`         | Project overview and technical documentation    |

Additional integration documentation and evidence are maintained in the repository's `docs/` and `evidence/` directories.

---

## 7. Security Considerations

This project is intended for local development and technical learning.

Current safeguards include:

* Synthetic patient and imaging data.

* Localhost-bound Docker host ports.

* Exclusion of generated and retrieved DICOM files from Git.

* Separation of development artifacts from production healthcare systems.

**Production deployment would require additional controls**, including authentication, TLS, access management, audit logging, monitoring, and appropriate handling of protected health information.

---

## 8. Current Limitations

The current HL7 imaging integration:

* Performs accession-based lookups against existing Orthanc studies.

* Does not automatically create DICOM studies from HL7 orders.

* Does not implement production EHR/PACS connectivity.

* Does not implement a complete radiology order lifecycle.

* Does not implement FHIR ImagingStudy mapping.

These capabilities remain outside the scope of the verified MVP.

---

## 9. Future Development

Planned enhancements include:

1\. Advanced HL7 ORM order lifecycle and radiology workflow integration.

2\. DICOM C-FIND study queries.

3\. DICOM C-MOVE retrieval workflows.

4\. DICOMweb exploration.

5\. FHIR ImagingStudy resource mapping.

6\. Healthcare imaging security controls.

---

## 10. Project Status

| Component                            | Status   |

| ------------------------------------ | -------- |

| Orthanc PACS deployment              | VERIFIED |

| DICOM C-ECHO connectivity            | VERIFIED |

| Synthetic DICOM generation           | VERIFIED |

| DICOM C-STORE transmission           | VERIFIED |

| DICOM retrieval and integrity        | VERIFIED |

| HL7 ORM accession-based study lookup | VERIFIED |

| Controlled negative-case handling    | VERIFIED |

| Positive regression testing          | VERIFIED |

| Advanced radiology interoperability  | PLANNED  |

| FHIR ImagingStudy integration        | PLANNED  |

---

**Akech Rose Medical Center (ARMC)**

*Healthcare Interoperability Engineering Portfolio*

**Project focus:** HL7 v2 | Mirth Connect | DICOM | Orthanc PACS | Healthcare Systems Integration
