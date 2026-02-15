-- ==========================================
-- SCHEMA: Operations Defect Recurrence System
-- PostgreSQL Compatible
-- ==========================================

-- =========================
-- TABLE: lots
-- =========================
CREATE TABLE lots (
    id BIGSERIAL PRIMARY KEY,
    lot_code VARCHAR(50) NOT NULL UNIQUE,
    production_date DATE NOT NULL,
    product_type VARCHAR(100) NOT NULL
);

-- =========================
-- TABLE: inspections
-- =========================
CREATE TABLE inspections (
    id BIGSERIAL PRIMARY KEY,
    lot_id BIGINT NOT NULL,
    inspection_date DATE NOT NULL,
    inspector_name VARCHAR(100) NOT NULL,

    CONSTRAINT fk_inspections_lot
        FOREIGN KEY (lot_id)
        REFERENCES lots(id)
        ON DELETE CASCADE
);

CREATE INDEX idx_inspections_lot_id ON inspections(lot_id);
CREATE INDEX idx_inspections_date ON inspections(inspection_date);

-- =========================
-- TABLE: defect_types
-- =========================
CREATE TABLE defect_types (
    id BIGSERIAL PRIMARY KEY,
    defect_name VARCHAR(150) NOT NULL UNIQUE,
    defect_description TEXT
);

-- =========================
-- TABLE: defect_occurrences
-- =========================
CREATE TABLE defect_occurrences (
    id BIGSERIAL PRIMARY KEY,
    inspection_id BIGINT NOT NULL,
    defect_type_id BIGINT NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    detected_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_occurrences_inspection
        FOREIGN KEY (inspection_id)
        REFERENCES inspections(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_occurrences_defect_type
        FOREIGN KEY (defect_type_id)
        REFERENCES defect_types(id)
        ON DELETE RESTRICT
);

CREATE INDEX idx_occurrences_inspection_id ON defect_occurrences(inspection_id);
CREATE INDEX idx_occurrences_defect_type_id ON defect_occurrences(defect_type_id);
CREATE INDEX idx_occurrences_quantity ON defect_occurrences(quantity);
