import pytest


@pytest.fixture
def sample_defects():
    """Sample defect data for testing."""
    return [
        {"id": "D001", "lot_id": "LOT001", "quantity": 5},
        {"id": "D001", "lot_id": "LOT002", "quantity": 3},
        {"id": "D002", "lot_id": "LOT001", "quantity": 2},
        {"id": "D003", "lot_id": "LOT003", "quantity": 0},
        {"id": "D004", "lot_id": "LOT004", "quantity": 1},
    ]


@pytest.fixture
def empty_defects():
    """Empty defect list for testing."""
    return []


@pytest.fixture
def single_zero_quantity():
    """Single defect with zero quantity."""
    return [{"id": "D001", "lot_id": "LOT001", "quantity": 0}]
