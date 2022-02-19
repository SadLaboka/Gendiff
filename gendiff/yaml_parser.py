import yaml


def yaml_to_dict(filepath: str) -> dict:
    """Parses YAML file and transforms to python dict"""
    with open(filepath, 'r') as file:
        result = yaml.load(file, Loader=yaml.FullLoader)
    return result
