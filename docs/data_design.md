# Data Design

## Overview

This document defines the core data entities and relationships derived from the Operations User Story and Acceptance Criteria for defect recurrence analysis.

The system aggregates inspection data from Excel files and identifies recurring defects across lots over time.

---

# AI Comparison Process

Two AI tools were used to extract data entities and relationships from the user story and ACs.

## AI 1 Output (More Technical & Structured)

AI 1 identified:
- Lot
- Inspection
- Defect
- DefectOccurrence

It emphasized normalization and recurrence calculation logic.
It clearly separated inspection records from defect records.

Strength:
- Strong relational modeling
- Better normalization thinking
- Clear many-to-many handling

Weakness:
- Did not explicitly model time aggregation
- Slightly over-engineered for small internal tool

---

## AI 2 Output (More Business-Oriented)

AI 2 identified:
- Lot
- DefectType
- InspectionLog
- DefectRecord

It focused more on business language and recurrence detection.
It included date fields and recurrence indicators more clearly.

Strength:
- Better alignment with user story language
- Strong time-awareness modeling
- Clear recurrence flag thinking

Weakness:
- Less precise relationship cardinality
- Slight redundancy between entities

---

# Final Merged Data Model

We merged both outputs to create a balanced, normalized, and business-aligned design.

---

# Entities & Attributes

## 1. Lot
Represents a production lot.

Attributes:
- lot_id (PK)
- production_date
- product_type

---

## 2. Inspection
Represents a single inspection event.

Attributes:
- inspection_id (PK)
- lot_id (FK)
- inspection_date
- inspector_name

Relationship:
- A Lot can have many Inspections
- Each Inspection belongs to one Lot

---

## 3. DefectType
Represents a category of defect.

Attributes:
- defect_type_id (PK)
- defect_name
- defect_description

---

## 4. DefectOccurrence
Represents an occurrence of a defect during an inspection.

Attributes:
- occurrence_id (PK)
- inspection_id (FK)
- defect_type_id (FK)
- quantity
- detected_at (timestamp)

Relationship:
- An Inspection can have many DefectOccurrences
- A DefectType can appear in many DefectOccurrences

---

# Relationships Summary

- Lot 1 --- N Inspection
- Inspection 1 --- N DefectOccurrence
- DefectType 1 --- N DefectOccurrence

This structure enables:
- Cross-lot defect detection
- Recurrence counting
- Excluding quantity = 0 rows
- Time-based aggregation

---

# Mermaid.js ERD

```mermaid
erDiagram

    LOT {
        string lot_id PK
        date production_date
        string product_type
    }

    INSPECTION {
        string inspection_id PK
        string lot_id FK
        date inspection_date
        string inspector_name
    }

    DEFECT_TYPE {
        string defect_type_id PK
        string defect_name
        string defect_description
    }

    DEFECT_OCCURRENCE {
        string occurrence_id PK
        string inspection_id FK
        string defect_type_id FK
        int quantity
        datetime detected_at
    }

    LOT ||--o{ INSPECTION : has
    INSPECTION ||--o{ DEFECT_OCCURRENCE : records
    DEFECT_TYPE ||--o{ DEFECT_OCCURRENCE : categorized_as
