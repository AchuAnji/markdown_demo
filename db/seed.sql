-- ==========================================
-- SIMPLE SEED (Defects, Lots, Inspections Only)
-- ==========================================

-- ==============================
-- Insert defect types
-- ==============================

INSERT INTO defect_types (defect_name, defect_description)
VALUES
('BURR', 'Raised edge'),
('CRACK', 'Surface crack'),
('POROSITY', 'Small holes'),
('WELD_DEFECT', 'Weld issue'),
('DIMENSIONAL', 'Out of tolerance');

-- ==============================
-- Insert lots
-- ==============================

INSERT INTO lots (lot_code, production_date, product_type)
VALUES
('LOT-001', '2025-12-15', 'Steel Beam'),
('LOT-002', '2025-12-16', 'Steel Beam'),
('LOT-003', '2025-12-17', 'Steel Plate'),
('LOT-004', '2025-12-18', 'Steel Rod'),
('LOT-005', '2025-12-19', 'Steel Beam');

-- ==============================
-- Insert inspections
-- ==============================

INSERT INTO inspections (lot_id, inspection_date, inspector_name)
VALUES
(1, '2025-12-16', 'Inspector A'),
(2, '2025-12-17', 'Inspector B'),
(3, '2025-12-18', 'Inspector C'),
(4, '2025-12-19', 'Inspector A'),
(5, '2025-12-20', 'Inspector B');
