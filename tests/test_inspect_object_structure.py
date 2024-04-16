import inspect_recursive as ipr


def test_inspect_object_structure():
    # Test case 1: Test with a simple dictionary
    simple_dict = {"a": 1, "b": 2, "c": 3}
    ipr.what(simple_dict)

    # Test case 2: Test with a nested dictionary
    nested_dict = {"a": {"x": 1, "y": 2}, "b": {"z": 3}}
    ipr.what(nested_dict)

    # Test case 3: Test with a list of strings
    list_of_strings = ["apple", "banana", "cherry"]
    ipr.what(list_of_strings)

    # Add more test cases as needed


if __name__ == "__main__":
    test_inspect_object_structure()
