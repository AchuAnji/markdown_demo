

class TestRecurringDefects:
    """Tests for identifying recurring defects (appearing in multiple lots)."""

    def test_identify_recurring_defects_basic(self, sample_defects):
        """Test identifying defects that appear in multiple lots."""
        from defect_dashboard.analytics import identify_recurring_defects

        recurring = identify_recurring_defects(sample_defects)
        assert "D001" in recurring
        assert len(recurring) == 1

    def test_recurring_defects_excludes_one_off(self, sample_defects):
        """Test that one-off defects are not included in recurring list."""
        from defect_dashboard.analytics import identify_recurring_defects

        recurring = identify_recurring_defects(sample_defects)
        assert "D002" not in recurring
        assert "D004" not in recurring

    def test_recurring_defects_returns_count(self, sample_defects):
        """Test that recurring defects include count of occurrences."""
        from defect_dashboard.analytics import identify_recurring_defects

        recurring = identify_recurring_defects(sample_defects)
        assert recurring.get("D001") == 2

    def test_recurring_defects_empty_list(self, empty_defects):
        """Test behavior with empty defect list."""
        from defect_dashboard.analytics import identify_recurring_defects

        recurring = identify_recurring_defects(empty_defects)
        assert recurring == {}

    def test_recurring_defects_all_different(self):
        """Test when all defects are one-off (different IDs)."""
        from defect_dashboard.analytics import identify_recurring_defects

        defects = [
            {"id": "D001", "lot_id": "LOT001", "quantity": 1},
            {"id": "D002", "lot_id": "LOT002", "quantity": 1},
            {"id": "D003", "lot_id": "LOT003", "quantity": 1},
        ]
        recurring = identify_recurring_defects(defects)
        assert recurring == {}

    def test_recurring_defects_multiple_recurring(self):
        """Test identifying multiple recurring defects."""
        from defect_dashboard.analytics import identify_recurring_defects

        defects = [
            {"id": "D001", "lot_id": "LOT001", "quantity": 1},
            {"id": "D001", "lot_id": "LOT002", "quantity": 1},
            {"id": "D002", "lot_id": "LOT003", "quantity": 1},
            {"id": "D002", "lot_id": "LOT004", "quantity": 1},
        ]
        recurring = identify_recurring_defects(defects)
        assert len(recurring) == 2
        assert recurring.get("D001") == 2
        assert recurring.get("D002") == 2
