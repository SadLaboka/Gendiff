def boolean_to_lower_str(source_dict: dict) -> None:
    """Transforms all True/False in dict values to true/false string"""
    for key, item in source_dict.items():
        if item is True:
            source_dict[key] = 'true'
        elif item is False:
            source_dict[key] = 'false'
