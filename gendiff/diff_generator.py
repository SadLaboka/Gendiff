from gendiff.parser import construct_dict
from gendiff.dict_comparator import compare_dicts
from gendiff.formatters.stylish import format_to_stylish


def generate_diff(path1: str, path2: str, output_format="stylish") -> str:
    """Generates difference between 2 files"""
    file1 = construct_dict(path1)
    file2 = construct_dict(path2)
    diff = compare_dicts(file1, file2)
    if output_format == "stylish":
        output = format_to_stylish(diff)
    return output
