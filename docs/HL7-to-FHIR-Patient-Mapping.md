# HL7 v2 to FHIR R4 Patient Mapping Specification

Project: HL7-FHIR Integration Lab
Interface: HL7_FHIR_PATIENT_V2
Source: Synthetic HL7 v2.5 ADT^A01
Destination: HAPI FHIR R4 Patient API
Integration Engine: Mirth Connect 4.4.0

## 1. Interface Purpose

Receive an HL7 ADT message, extract patient demographics,
transform selected fields into FHIR R4 format, and send
a Patient resource to HAPI FHIR.

## 2. Field Mapping

| HL7 Field | Description | FHIR Field | Transformation |
|-----------|-------------|------------|----------------|
| PID-3.1 | Patient MRN | Patient.identifier.value | Copy |
| PID-5.1 | Family name | Patient.name.family | Copy |
| PID-5.2 | Given name | Patient.name.given | Copy |
| PID-7 | Date of birth | Patient.birthDate | YYYYMMDD to YYYY-MM-DD |
| PID-8 | Administrative sex | Patient.gender | M=male, F=female, O=other, otherwise unknown |

## 3. Identifier System

Patient.identifier.system:
https://neema.example.org/mrn

The MRN is stored in Patient.identifier.value.

The FHIR server assigns Patient.id independently.

## 4. Example

Input HL7:

PID|1||TEST10003^^^NEEMA^MR||SMITH^JOHN||19851225|M

Expected FHIR fields:

identifier.value = TEST10003
name.family = SMITH
name.given = JOHN
birthDate = 1985-12-25
gender = male

## 5. Verified Test Results

Test Patient 1:
MRN: TEST10002
FHIR Resource: Patient/1000
Result: Successfully retrieved through FHIR REST API.

Test Patient 2:
MRN: TEST10003
FHIR Resource: Patient/1001
Result: Successfully retrieved through FHIR REST API.

## 6. Current Scope

Implemented:
- HL7 ADT message reception over TCP/MLLP
- Patient demographic extraction
- JavaScript field transformation
- FHIR Patient JSON construction
- HTTP POST to HAPI FHIR
- REST API retrieval verification

Not yet implemented:
- Encounter resource mapping
- Observation resource mapping
- Duplicate-patient prevention
- Production-grade validation and error handling

Note: All patient information is synthetic.
