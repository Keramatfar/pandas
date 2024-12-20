"""
This module contains a test for the `value_counts` function with the new 'keep' parameter.
"""

import pandas as pd

def test_value_counts_normalize():
    """This function tests the ability of the value_counts function with the keep parameter."""
    # Test data
    data = pd.Series([1, 1, 2, 2, 3, 3, 3, 4])

    # Apply the function to the series (with the 'keep' parameter introduced)
    result = data.value_counts(normalize='keep')  # Assuming your new feature is applied

    # Expected output: Normalized value counts
    expected = pd.Series(
        {3: '3(0.375)', 1: '2(0.25)', 2: '2(0.25)', 4: '1(0.125)'},
        name="proportion"  # Ensure the name is set here to match the result
    )

    # Ensure both result and expected have the same name attribute
    pd.testing.assert_series_equal(result, expected, check_names=True)
