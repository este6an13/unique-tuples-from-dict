def get_tuples(similar_ids):
    """
    Generate unique tuples of similar IDs.

    Args:
        similar_ids (dict): A dictionary containing IDs and their similar IDs.

    Returns:
        set: A set of unique tuples containing pairs of similar IDs.

    """
    tuples_list = []
    for id_, sids in similar_ids.items():
        # we obtain list of sorted lists of two elements each
        pairs = [sorted([id_, sid]) for sid in sids]
        for pair in pairs:
            # for each pair, we convert it into a tuple
            tuples_list.append(tuple(pair))
    # list conversion to set, to remove duplicates
    tuples_set = set(tuples_list)
    return tuples_set

def test_get_tuples():
    # Test case 1
    similar_ids = {
        123: [458, 812, 765],
        458: [123, 812, 765],
        812: [123, 458],
        765: [123, 458],
        999: [100],
        100: [999]
    }
    expected_result = {(458, 765), (123, 765), (100, 999), (123, 812), (123, 458), (458, 812)}
    result = get_tuples(similar_ids)
    assert result == expected_result, f"Test case 1 failed. Expected: {expected_result}, Got: {result}"

    # Test case 2
    similar_ids = {
        1: [2, 3, 4],
        2: [1, 3],
        3: [1, 2, 4],
        4: [1, 3]
    }
    expected_result = {(1, 2), (1, 3), (1, 4), (2, 3), (3, 4)}
    result = get_tuples(similar_ids)
    assert result == expected_result, f"Test case 2 failed. Expected: {expected_result}, Got: {result}"

    # Test case 3
    similar_ids = {
        10: [20, 30],
        20: [10, 30],
        30: [10, 20]
    }
    expected_result = {(10, 20), (10, 30), (20, 30)}
    result = get_tuples(similar_ids)
    assert result == expected_result, f"Test case 3 failed. Expected: {expected_result}, Got: {result}"


    print("All test cases passed!")

# Run the tests
test_get_tuples()