"""Core analytics module for defect recurrence analysis."""

from typing import List, Dict


def identify_recurring_defects(defects: List[Dict]) -> Dict:
    """
    Identify recurring defects (appearing in multiple lots).
    
    Args:
        defects: List of defect records with 'id', 'lot_id', and 'quantity' keys
        
    Returns:
        Dictionary mapping defect_id to count of lots where it appears
        Only includes defects with quantity > 0
    """
    if not defects:
        return {}
    
    # Count unique lots for each defect (excluding zero quantities)
    defect_lot_count = {}
    
    for defect in defects:
        if defect.get('quantity', 0) > 0:  # Exclude zero-quantity defects
            defect_id = defect['id']
            lot_id = defect['lot_id']
            
            # Track unique lots for each defect
            if defect_id not in defect_lot_count:
                defect_lot_count[defect_id] = set()
            
            defect_lot_count[defect_id].add(lot_id)
    
    # Return only defects that appear in multiple lots
    recurring = {}
    for defect_id, lots in defect_lot_count.items():
        if len(lots) > 1:
            recurring[defect_id] = len(lots)
    
    return recurring

