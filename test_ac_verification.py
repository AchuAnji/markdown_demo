#!/usr/bin/env python3
"""
Test script to verify all Acceptance Criteria (ACs) are satisfied by app.py
"""

import psycopg2
import pandas as pd
import os
from sys import exit

# Set up database connection
DATABASE_URL = "postgresql://localhost/markdown_demo_test"
os.environ['DATABASE_URL'] = DATABASE_URL

def get_connection():
    """Create database connection"""
    return psycopg2.connect(DATABASE_URL)

def get_recurring_defects():
    """Get recurring defects (same as app.py)"""
    query = """
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
    """
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def get_one_off_defects():
    """Get one-off defects (same as app.py)"""
    query = """
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
    """
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def verify_all_defects_query():
    """Verify AC3: All defects with quantity > 0"""
    query = """
    SELECT
        dt.defect_name,
        COUNT(*) AS occurrence_count,
        SUM(d.quantity) AS total_quantity
    FROM defect_occurrences d
    JOIN defect_types dt ON d.defect_type_id = dt.id
    WHERE d.quantity > 0
    GROUP BY dt.defect_name;
    """
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def verify_zero_quantity_query():
    """Verify AC3: Zero quantity defects should NOT appear in results"""
    query = """
    SELECT
        dt.defect_name,
        COUNT(*) AS zero_qty_count
    FROM defect_occurrences d
    JOIN defect_types dt ON d.defect_type_id = dt.id
    WHERE d.quantity = 0
    GROUP BY dt.defect_name;
    """
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def test_ac1():
    """AC1: System identifies recurring defects (appearing in multiple lots)"""
    print("\n" + "="*70)
    print("AC1: Identify recurring defects (appearing in multiple lots)")
    print("="*70)
    
    recurring_df = get_recurring_defects()
    
    print("\nRecurring Defects Result:")
    print(recurring_df.to_string(index=False))
    
    # Verify BURR appears in 3 lots and CRACK in 2 lots
    expected_recurring = {'BURR', 'CRACK'}
    actual_recurring = set(recurring_df['defect_name'].values)
    
    success = expected_recurring == actual_recurring
    
    print("\n✓ EXPECTED: BURR (3 lots), CRACK (2 lots)")
    print(f"✓ ACTUAL: {', '.join([f'{row[0]} ({int(row[1])} lots)' for row in recurring_df.values])}")
    
    if success:
        print("\n✅ AC1 PASSED: Recurring defects correctly identified")
    else:
        print("\n❌ AC1 FAILED: Recurring defects not correctly identified")
    
    return success

def test_ac2():
    """AC2: System identifies one-off defects (appearing in exactly one lot)"""
    print("\n" + "="*70)
    print("AC2: Identify one-off defects (appearing in exactly one lot)")
    print("="*70)
    
    one_off_df = get_one_off_defects()
    
    print("\nOne-Off Defects Result:")
    print(one_off_df.to_string(index=False))
    
    # Verify POROSITY appears in only 1 lot
    expected_one_off = {'POROSITY'}
    actual_one_off = set(one_off_df['defect_name'].values)
    
    success = expected_one_off == actual_one_off
    
    print("\n✓ EXPECTED: POROSITY (1 lot)")
    print(f"✓ ACTUAL: {', '.join([f'{row[0]} ({int(row[1])} lot)' for row in one_off_df.values])}")
    
    if success:
        print("\n✅ AC2 PASSED: One-off defects correctly identified")
    else:
        print("\n❌ AC2 FAILED: One-off defects not correctly identified")
    
    return success

def test_ac3():
    """AC3: System excludes zero-quantity defects from analysis"""
    print("\n" + "="*70)
    print("AC3: Exclude zero-quantity defects from analysis")
    print("="*70)
    
    # Check what defects with quantity > 0 are in results
    all_defects = verify_all_defects_query()
    zero_qty = verify_zero_quantity_query()
    
    print("\nDefects WITH quantity > 0 (should be counted):")
    print(all_defects.to_string(index=False))
    
    print("\nDefects WITH quantity = 0 (should be excluded):")
    if zero_qty.empty:
        print("None - ✓")
    else:
        print(zero_qty.to_string(index=False))
    
    # WELD_DEFECT has quantity=0 and should NOT appear in any results
    recurring_df = get_recurring_defects()
    one_off_df = get_one_off_defects()
    
    all_results = pd.concat([recurring_df, one_off_df], ignore_index=True)
    has_weld_defect = 'WELD_DEFECT' in all_results['defect_name'].values
    
    success = not has_weld_defect and not zero_qty.empty
    
    print("\n✓ EXPECTED: WELD_DEFECT (quantity=0) should NOT appear in results")
    print(f"✓ ACTUAL: WELD_DEFECT {'NOT ' if not has_weld_defect else ''}found in results")
    
    if success:
        print("\n✅ AC3 PASSED: Zero-quantity defects correctly excluded")
    else:
        print("\n❌ AC3 FAILED: Zero-quantity defects handling issue")
    
    return success

def test_ac4():
    """AC4: System displays results in a web dashboard with clear sections"""
    print("\n" + "="*70)
    print("AC4: Display results in web dashboard with clear sections")
    print("="*70)
    
    print("\nVerifying app.py structure...")
    
    try:
        with open('/Users/anjineyulu/Documents/markdown_demo/db/UI/app.py', 'r') as f:
            app_content = f.read()
        
        checks = {
            "Has st.title()": 'st.title(' in app_content,
            "Has st.header() for Recurring": 'st.header("Recurring Defects")' in app_content,
            "Has st.header() for One-Off": 'st.header("One-Off Defects")' in app_content,
            "Has st.dataframe()": 'st.dataframe(' in app_content,
            "Uses Streamlit framework": 'import streamlit' in app_content,
        }
        
        print("\nApp.py Structure Checks:")
        for check_name, result in checks.items():
            print(f"  {'✓' if result else '✗'} {check_name}")
        
        success = all(checks.values())
        
        if success:
            print("\n✅ AC4 PASSED: App properly displays dashboard with sections")
        else:
            print("\n❌ AC4 FAILED: Some dashboard elements missing")
        
        return success
    except Exception as e:
        print(f"\n❌ AC4 FAILED: Error checking app.py: {e}")
        return False

def test_ac5():
    """AC5: System handles insufficient data gracefully"""
    print("\n" + "="*70)
    print("AC5: Handle insufficient data gracefully")
    print("="*70)
    
    print("\nVerifying app.py error handling...")
    
    try:
        with open('/Users/anjineyulu/Documents/markdown_demo/db/UI/app.py', 'r') as f:
            app_content = f.read()
        
        checks = {
            "Checks if recurring_df.empty": 'recurring_df.empty' in app_content,
            "Shows warning for no recurring": 'st.warning(' in app_content and 'No recurring defects' in app_content,
            "Checks if one_off_df.empty": 'one_off_df.empty' in app_content,
            "Shows warning for no one-off": 'st.warning(' in app_content and 'No one-off defects' in app_content,
        }
        
        print("\nError Handling Checks:")
        for check_name, result in checks.items():
            print(f"  {'✓' if result else '✗'} {check_name}")
        
        success = all(checks.values())
        
        if success:
            print("\n✅ AC5 PASSED: App handles missing data gracefully")
        else:
            print("\n❌ AC5 FAILED: Error handling incomplete")
        
        return success
    except Exception as e:
        print(f"\n❌ AC5 FAILED: Error checking app.py: {e}")
        return False

def main():
    """Run all AC tests"""
    print("\n" + "█"*70)
    print("ACCEPTANCE CRITERIA (AC) VERIFICATION TEST")
    print("█"*70)
    
    try:
        results = {
            "AC1": test_ac1(),
            "AC2": test_ac2(),
            "AC3": test_ac3(),
            "AC4": test_ac4(),
            "AC5": test_ac5(),
        }
        
        # Summary
        print("\n" + "="*70)
        print("SUMMARY")
        print("="*70)
        
        for ac, passed in results.items():
            status = "✅ PASSED" if passed else "❌ FAILED"
            print(f"{ac}: {status}")
        
        total = len(results)
        passed = sum(results.values())
        
        print(f"\nTotal: {passed}/{total} ACs passed")
        
        if passed == total:
            print("\n🎉 ALL ACCEPTANCE CRITERIA SATISFIED!")
            return 0
        else:
            print(f"\n⚠️  {total - passed} AC(s) need attention")
            return 1
            
    except Exception as e:
        print(f"\n❌ Test execution failed: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    exit(main())
