

class TestOneOffDefects:
    """Tests for identifying one-off defects (appearing in single lot)."""

    def test_identify_oneoff_defects_basic(self, sample_defects):
        """Test identifying defects that appear in only one lot."""
        from defect_dashboard.analytics import identify_oneoff_defects

        oneoff = identify_oneoff_defects(sample_defects)
        assert "D002" in oneoff
        assert "D004" in oneoff
        assert len(oneoff) == 2

    def test_oneoff_defects_excludes_recurring(self, sample_defects):
        """Test that recurring defects are not included in one-off list."""
        from defect_dashboard.analytics import identify_oneoff_defects

        oneoff = identify_oneoff_defects(sample_defects)
        assert "D001" not in oneoff

    def test_oneoff_defects_returns_lot_info(self, sample_defects):
        """Test that one-off defects include their lot information."""
        from defect_dashboard.analytics import identify_oneoff_defects

        oneoff = identify_oneoff_defects(sample_defects)
        assert oneoff.get("D002") == "LOT001"
        assert oneoff.get("D004") == "LOT004"

    def test_oneoff_defects_empty_list(self, empty_defects):
        """Test behavior with empty defect list."""
        from defect_dashboard.analytics import identify_oneoff_defects

        oneoff = identify_oneoff_defects(empty_defects)
        assert oneoff == {}

    def test_oneoff_defects_all_unique(self):
        """Test when all defects are one-off (all different IDs)."""
        from defect_dashboard.analytics import identify_oneoff_defects

        defects = [
            {"id": "D001", "lot_id": "LOT001", "quantity": 1},
            {"id": "D002", "lot_id": "LOT002", "quantity": 1},
            {"id": "D003", "lot_id": "LOT003", "quantity": 1},
        ]
        oneoff = identify_oneoff_defects(defects)
        assert len(oneoff) == 3

    def test_oneoff_defects_no_oneoff_exists(self):
        """Test when no one-off defects exist (all recurring)."""
        from defect_dashboard.analytics import identify_oneoff_defects

        defects = [
            {"id": "D001", "lot_id": "LOT001", "quantity": 1},
            {"id": "D001", "lot_id": "LOT002", "quantity": 1},
            {"id": "D002", "lot_id": "LOT003", "quantity": 1},
            {"id": "D002", "lot_id": "LOT004", "quantity": 1},
        ]
        oneoff = identify_oneoff_defects(defects)
        assert oneoff == {}
