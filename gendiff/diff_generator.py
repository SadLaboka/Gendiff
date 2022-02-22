from gendiff.parser import construct_dict
from gendiff.dict_comparator import compare_dicts
from gendiff.formatters.stylish import format_to_json


def generate_diff(filepath1: str, filepath2: str) -> str:
    """Generates difference between 2 files"""
    file1 = construct_dict(filepath1)
    file2 = construct_dict(filepath2)
    diff = compare_dicts(file1, file2)
    output = format_to_json(diff)
    return output
