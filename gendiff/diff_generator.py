from gendiff.yaml_parser import yaml_to_dict
from gendiff.json_parser import json_to_dict
from gendiff.bool_transformer import boolean_to_lower_str


def parser_selector(filepath: str):
    """Selects a parser for each file format"""
    file_extension = filepath.split('.')[-1]
    if file_extension in ('yml', 'yaml'):
        return yaml_to_dict(filepath)
    elif file_extension == 'json':
        return json_to_dict(filepath)


def generate_diff(filepath1: str, filepath2: str) -> str:
    """Generates difference between 2 files"""
    file1 = parser_selector(filepath1)
    boolean_to_lower_str(file1)
    file2 = parser_selector(filepath2)
    boolean_to_lower_str(file2)
    set_of_keys = set(file1)
    set_of_keys.update(file2)
    difference = '{\n'
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
