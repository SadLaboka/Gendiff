import json


def generate_diff(filepath1: str, filepath2: str) -> str:
    """Generates difference between 2 files"""
    difference = '{\n'
    file1 = json_parser(filepath1)
    file2 = json_parser(filepath2)
    set_of_keys = set(file1)
    set_of_keys.update(file2)
    for key in sorted(set_of_keys):
        if key in file1 and key not in file2:
            difference += f'  - {key}: {file1[key]}\n'
        elif key not in file1 and key in file2:
            difference += f'  + {key}: {file2[key]}\n'
        elif key in file1 and key in file2:
            if file1[key] != file2[key]:
                difference += f'  - {key}: {file1[key]}\n'
                difference += f'  + {key}: {file2[key]}\n'
            else:
                difference += f'    {key}: {file1[key]}\n'
    return difference + '}'


def json_parser(filepath: str) -> dict:
    """Parses json file and transforms to python dict"""
    result = json.load(open(filepath))
    for key, item in result.items():
        if item is True or item is False:
            result.update({key: boolean_to_lower_str(item)})
    return result


def boolean_to_lower_str(value: bool) -> str:
    """Transforms python True/False to true/false string"""
    return 'true' if value else 'false'
