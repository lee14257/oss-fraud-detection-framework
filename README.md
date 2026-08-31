# Open-Source Real-Time Fraud Detection Framework (`oss-fraud-detection-framework`)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()

An open-source, modular, low-latency framework designed for real-time financial fraud detection, event-driven rule condition evaluation, stateful feature transformation, and immutable audit logging. 

This project provides financial institutions, payment processors, and mid-sized organizations with an accessible, production-grade reference architecture to replace disjointed or legacy fraud stacks.

---

## Key System Modules

1. **Streaming Event Ingestion (`src/ingestion/`)**
   - Strongly typed, immutable transaction event models (`TransactionEvent`).
   - Standardized schemas for financial transaction payloads, device signals, and network telemetry.

2. **Condition Evaluation Engine (`src/rules/`)**
   - Decoupled, modular rule engine architecture allowing condition-by-condition evaluation (`Condition`, `RuleEngine`).
   - Granular execution visibility designed to reduce false positives and enable instant rule tuning without engine downtime.
   - Low-latency SLA enforcement (<50ms target per evaluation cycle).

3. **Stateful Feature Transformation (`src/features/`)** *(In Active Development)*
   - Interfaces for real-time aggregation and windowed feature computation (e.g., account velocity, IP frequency, transaction historical deltas).

4. **Immutable Decision & Compliance Auditor (`src/audit/`)**
   - Structured JSON audit logger (`AuditLogger`) capturing transaction IDs, rule outcome verdicts, condition breakdown maps, and microsecond-level execution latencies.
   - Built to support strict regulatory auditability and compliance standards.

---

## Architecture & System Flow
[ Financial Transaction Event ]
                 │
                 ▼
    1. Event Ingestion Layer
      (`TransactionEvent`)
                 │
                 ▼
    2. Rule Condition Evaluator ────► Condition Breakdown Map
         (`RuleEngine`)
                 │
                 ▼
    3. Compliance Audit Logger  ────► Structured JSON Logs
         (`AuditLogger`)

---

## Getting Started

### Prerequisites
- Python 3.9+

### Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/lee14257/oss-fraud-detection-framework.git
   cd oss-fraud-detection-framework

2. Run the unit test suite:
    ```bash
    python3 -m unittest discover -s tests