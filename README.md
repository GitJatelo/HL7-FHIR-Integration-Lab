# Akech Rose Medical Center (ARMC)
## HL7 v2 → FHIR R4 Healthcare Interoperability Lab

**Project:** ARMC Healthcare Interoperability Initiative  
**Environment:** Mirth Connect 4.4.0 | HAPI FHIR R4 | Docker | PostgreSQL | Microsoft Azure

### Project Overview

Akech Rose Medical Center (ARMC) is a simulated healthcare
environment developed to demonstrate HL7 v2 messaging,
FHIR R4 interoperability, interface engineering,
and cloud integration.

The project includes a verified HL7 ADT^A01 workflow
that performs FHIR Patient lookup and reuse,
followed by Encounter creation and REST API verification.

All patient information used in this project is synthetic and intended solely for educational, testing, and demonstration purposes.


### Technical Identifier Compatibility

This project was originally developed under the
NEEMA Hospital simulation.

Existing NEEMA HL7 assigning authorities, FHIR identifier
systems, Mirth channel names, and verified resources
are intentionally preserved for compatibility.

ARMC is the official public-facing project identity.

## Technologies

- Mirth Connect 4.4.0
- HL7 v2.5
- FHIR R4
- JavaScript
- HAPI FHIR Server
- Docker
- PostgreSQL
- PowerShell
- Git and GitHub (public project repository)

## Integration Architecture

### Verified Local Integration Architecture

```text
ARMC Synthetic HL7 ADT^A01
            |
            v
     TCP / MLLP Listener
     Mirth Connect :6665
            |
            v
     HL7 Message Processing
            |
            v
      FHIR Patient Lookup
            |
       +----+----+
       |         |
       v         v
    Existing    New
    Patient     Patient
       |         |
       |     Patient Create
       |         |
       +----+----+
            |
            v
     FHIR Encounter Create
            |
            v
     HAPI FHIR R4 :8081
            |
            v
     REST API Verification
```

## Implemented Features

### HL7 Message Processing

- HL7 v2.5 ADT^A01 message reception
- Patient identifier extraction from PID-3
- Patient name and demographic mapping
- Date-of-birth formatting
- Administrative sex-to-FHIR gender mapping
- Encounter class extraction from PV1
- JavaScript-based HL7-to-FHIR transformation

### FHIR Patient Integration

- MRN-based Patient lookup using the FHIR REST API
- Existing Patient identification and reuse
- Conditional Patient creation workflow
- FHIR Patient JSON generation
- Independent Patient resource verification

### FHIR Encounter Integration

- FHIR Encounter JSON generation
- Patient-to-Encounter reference mapping
- Emergency Encounter class mapping (EMER)
- HTTP POST Encounter creation
- HTTP 201 Created response verification
- Encounter ID extraction
- Independent Encounter retrieval using the FHIR REST API
## Verified Test Results

| Test | MRN | FHIR Resource | Result |
|---|---|---|---|
| Patient retrieval | TEST10002 | Patient/1000 | Verified |
| Patient retrieval | TEST10003 | Patient/1001 | Verified |
| Patient lookup and reuse | TEST10003 | Patient/1001 | Verified |
| Encounter creation | TEST10003 | Encounter/1003 | HTTP 201 Created |
| Encounter retrieval | TEST10003 | Encounter/1003 | Verified |
| Encounter patient reference | TEST10003 | Patient/1001 | Verified |

FHIR resource IDs are assigned by the server and may
differ between installations or test runs.

## Repository Structure

```text
HL7-FHIR-Integration-Lab/
├── docs/
├── evidence/
├── fhir-resources/
├── hl7-samples/
├── mirth-channels/
├── .gitignore
└── README.md
```

## Current Limitations

- Duplicate Encounter prevention is not yet implemented.
- Patient lookup and reuse are implemented, but comprehensive duplicate-patient handling requires additional testing.
- HL7 field validation and error handling require further development.
- ADT discharge, transfer, and demographic update workflows are not yet implemented.
- ORU-to-FHIR Observation integration is pending.
- Automated integration and regression testing are not yet implemented.
- Production-grade security, authentication, and monitoring are not configured.
- End-to-end Azure-hosted HL7/FHIR integration has not yet been verified.

## Planned Enhancements

1. Implement PV1-19 visit number mapping to FHIR Encounter.identifier.
2. Implement Encounter lookup and duplicate Encounter prevention.
3. Implement ADT^A03 discharge processing and Encounter status updates.
4. Implement ADT^A02 patient transfer and ADT^A08 demographic updates.
5. Develop ORM^O01 order processing and ORU^R01 laboratory result integration.
6. Map OBR and OBX segments to FHIR Observation and DiagnosticReport resources.
7. Implement DFT^P03 financial transaction processing.
8. Strengthen HL7 validation, ACK handling, error logging, and troubleshooting.
9. Develop automated integration and regression tests.
10. Complete Azure infrastructure configuration and validate secure hybrid HL7/FHIR integration.
11. Document deployment procedures, interface specifications, and operational runbooks.

## Security and Privacy

This project uses synthetic training data only.

It is not intended for production use.

Do not commit real patient information, passwords,
API credentials, or other sensitive information.

## Author

Robert Osano

Healthcare Interoperability Portfolio Project
