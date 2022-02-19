import json


def json_to_dict(filepath: str) -> dict:
    """Parses json file and transforms to python dict"""
    result = json.load(open(filepath))
    return result
