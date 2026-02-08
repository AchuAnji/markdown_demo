# Assumptions & Scope

## Assumptions

### Assumption 1: Common Relational Key
We assume all Excel files contain a common key (e.g., `Lot_ID`) that enables relational mapping across files, even if column names or key formats differ slightly.

### Assumption 2: Excel as Source of Truth
Instead of a live database, Excel files are treated as the **Source of Truth**, simulating exports from a legacy or older ERP system.

---

## In Scope

- Identifying whether the same defect type appears across multiple lots over time
- Distinguishing recurring defect issues from one-off incidents
- Aggregating inspection data across daily and weekly inspection logs
- Excluding non-defect inspection records (e.g., `Qty Defects = 0`) from defect occurrence counts
- Indicating when available data is insufficient to determine defect recurrence

---

## Out of Scope

- Root cause analysis of defects
- Predictive or AI-based quality analysis
- Real-time inspection or production monitoring
- Enforcement of data correctness at the source (e.g., preventing invalid Excel entries)
- User authentication, authorization, or role-based access control
- Pixel-perfect or consumer-grade UI/UX design (focus is on functionality and clarity)
