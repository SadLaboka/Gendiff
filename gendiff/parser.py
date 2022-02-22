import json
import yaml


def construct_dict(filepath: str) -> dict:
    """Constructs dict from source file"""
    file_extension = filepath.split('.')[-1]
    if file_extension in ('yml', 'yaml'):
        result_dict = yaml.load(open(filepath), Loader=yaml.FullLoader)
    elif file_extension == 'json':
        result_dict = json.load(open(filepath))
    boolean_to_lower_str(result_dict)
    return result_dict


def boolean_to_lower_str(source_dict: dict) -> None:
    """Transforms all True/False in dict values to true/false string"""
    for key, item in source_dict.items():
        if isinstance(item, dict):
            boolean_to_lower_str(item)
        if item is True:
            source_dict[key] = 'true'
        elif item is False:
            source_dict[key] = 'false'
        elif isinstance(item, type(None)):
            source_dict[key] = 'null'
