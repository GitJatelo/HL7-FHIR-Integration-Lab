# HL7 v2 to FHIR R4 Integration Lab

## Project Overview

This project demonstrates a local healthcare interoperability
workflow using HL7 v2.5, Mirth Connect, and HAPI FHIR R4.

The interface receives synthetic HL7 ADT messages, extracts
patient demographics, transforms them into FHIR Patient
resources, and submits them to a FHIR REST API.

All patient information is synthetic.

## Technologies

- Mirth Connect 4.4.0
- HL7 v2.5
- FHIR R4
- JavaScript
- HAPI FHIR Server
- Docker
- PostgreSQL
- PowerShell
- Git and GitHub (repository publication planned)

## Integration Architecture

HL7 ADT Sender
       |
       v
TCP / MLLP Listener
Port 6664
       |
       v
Mirth Connect
JavaScript Transformer
       |
       v
FHIR Patient JSON
       |
       v
HTTP POST /fhir/Patient
       |
       v
HAPI FHIR R4 Server
Port 8081
       |
       v
FHIR Resource Storage

## Implemented Features

- HL7 ADT message reception
- Patient identifier extraction
- Patient name mapping
- Date-of-birth formatting
- Administrative sex-to-FHIR gender mapping
- FHIR Patient JSON generation
- HTTP POST to HAPI FHIR
- Independent REST API verification

## Verified Test Results

| Test | MRN | FHIR Resource | Result |
|------|-----|---------------|--------|
| 1 | TEST10002 | Patient/1000 | Retrieved successfully |
| 2 | TEST10003 | Patient/1001 | Retrieved successfully |

FHIR resource IDs are assigned by the server and may
differ between installations or test runs.

## Repository Structure

docs/
    HL7-to-FHIR-Patient-Mapping.md

evidence/
    patient-1000.json
    patient-1001.json

hl7-samples/
    ADT_A01_TEST10003.hl7

mirth-channels/
    HL7_FHIR_PATIENT_V2.xml

fhir-resources/
    Planned reusable FHIR examples

## Current Limitations

- No duplicate-patient prevention
- Limited field validation
- No Encounter resource generation
- No Observation resource generation
- No automated integration test suite
- No production security configuration

## Planned Enhancements

1. Add Encounter mapping using PV1.
2. Add ORU-to-FHIR Observation mapping.
3. Implement validation and error handling.
4. Add automated integration tests.
5. Document deployment and troubleshooting.
6. Explore Azure, AWS, and GCP deployment options.

## Security and Privacy

This project uses synthetic training data only.

It is not intended for production use.

Do not commit real patient information, passwords,
API credentials, or other sensitive information.

## Author

Robert Osano

Healthcare Interoperability Portfolio Project
