-- ==========================================
-- SAMPLE QUERIES
-- ==========================================

-- 1️⃣ Exclude zero-quantity defects (AC requirement)
SELECT *
FROM defect_occurrences
WHERE quantity > 0;

-- 2️⃣ Detect recurring defects across multiple lots
SELECT
    dt.defect_name,
    COUNT(DISTINCT l.id) AS affected_lots
FROM defect_occurrences d
JOIN inspections i ON d.inspection_id = i.id
JOIN lots l ON i.lot_id = l.id
JOIN defect_types dt ON d.defect_type_id = dt.id
WHERE d.quantity > 0
GROUP BY dt.defect_name
HAVING COUNT(DISTINCT l.id) > 1;

-- 3️⃣ One-off defects
SELECT
    dt.defect_name,
    COUNT(DISTINCT l.id) AS affected_lots
FROM defect_occurrences d
JOIN inspections i ON d.inspection_id = i.id
JOIN lots l ON i.lot_id = l.id
JOIN defect_types dt ON d.defect_type_id = dt.id
WHERE d.quantity > 0
GROUP BY dt.defect_name
HAVING COUNT(DISTINCT l.id) = 1;

-- 4️⃣ Weekly aggregation
SELECT
    DATE_TRUNC('week', i.inspection_date) AS week_start,
    dt.defect_name,
    SUM(d.quantity) AS total_defects
FROM defect_occurrences d
JOIN inspections i ON d.inspection_id = i.id
JOIN defect_types dt ON d.defect_type_id = dt.id
WHERE d.quantity > 0
GROUP BY week_start, dt.defect_name
ORDER BY week_start;
