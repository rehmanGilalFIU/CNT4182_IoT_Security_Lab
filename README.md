# IoT Smart Building Management System
## CNT 4182 – Mobile and IoT Cybersecurity

### 1. Project Overview

This repository contains a Python-based IoT Smart Building Management System developed for cybersecurity analysis and educational research.

The application simulates a connected smart building environment where users, administrators, IoT devices, and sensors interact through software services and APIs.

The project is designed to support the identification, classification, and evaluation of cybersecurity weaknesses in IoT-enabled software applications.

### 2. Application Features

The system includes several interconnected components:

- **User Authentication:** User registration, login, and account management.
- **IoT Device Management:** Device registration, configuration, monitoring, and control.
- **Sensor Monitoring:** Collection and processing of simulated environmental sensor data.
- **Database Management:** Storage and retrieval of users, devices, and telemetry records.
- **Administrative Functions:** Management of system users, devices, and configuration.
- **API Services:** Communication between application components and connected devices.
- **Firmware Management:** Simulated firmware update operations.
- **Reporting and Logging:** Generation of system reports and operational records.

### 3. Technology Stack

- **Programming Language:** Python
- **Web Framework:** Flask
- **Database:** SQLite
- **Architecture:** Modular web application with simulated IoT functionality
- **Security Analysis:** Static Application Security Testing (SAST)

### 4. Cybersecurity Assessment Objectives

The primary objective is to evaluate the security of the application by examining its source code.

Security analysts should:

1. Examine the application's architecture and functionality.
2. Identify potential cybersecurity vulnerabilities.
3. Determine the affected files and code locations.
4. Classify identified weaknesses using appropriate CWE categories.
5. Assess the potential security impact.
6. Recommend appropriate mitigation measures.

The application may contain intentional security weaknesses. Their types, locations, and total number are not disclosed.

### 5. Security Analysis Approaches

The source code can be evaluated using different approaches.

**Traditional Security Analysis**

Use a source-code security scanner, such as Semgrep or Snyk Code, to identify potential vulnerabilities through static analysis.

**AI-Assisted Security Analysis**

Use a Generative AI system, such as ChatGPT, to examine the same source code and identify potential cybersecurity weaknesses.

Both approaches should analyze the same version of the application.

### 6. Expected Findings

For every identified security issue, report:

| Field       | Description |
|-------------|-------------|
| Finding ID  | Unique identifier |
| Vulnerability | Name of the identified weakness |
| File / Line | Location in source code |
| CWE ID | Relevant weakness classification |
| Severity | Critical, High, Medium, or Low |
| Evidence | Relevant code and explanation |
| Impact | Potential security consequences |
| Recommendation | Suggested remediation |

Findings should be supported by evidence. A scanner warning or AI-generated claim should not automatically be considered a confirmed vulnerability.

### 7. Important Security Notice

**This application is intentionally designed for cybersecurity education and controlled security testing.**

- Do not deploy it to production environments.
- Do not expose it to the public internet.
- Do not use real credentials or sensitive personal information.
- Conduct any runtime testing only in authorized, isolated environments.
- The application is not intended for real building automation or physical IoT device control.

### 8. Academic Purpose

This repository supports practical learning and comparative evaluation of cybersecurity vulnerability detection techniques.

It may be used to study the strengths and limitations of conventional security scanning tools and AI-assisted source-code analysis.

---

**Course:** CNT 4182 – Mobile and IoT Cybersecurity  
**Purpose:** Cybersecurity Education and Research
