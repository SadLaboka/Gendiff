from gendiff.status_constants import (
    ADDED,
    REMOVED,
    NESTED,
    CHANGED,
    UNCHANGED
)


def compare_dicts(first_dict: dict, second_dict: dict) -> dict:
    """Compares 2 dicts"""
    keys = sorted(set(first_dict) | set(second_dict))
    return {key: generate_tree_node(
        key,
        first_dict,
        second_dict
    ) for key in keys}


def generate_tree_node(key, first_dict: dict, second_dict: dict) -> dict:
    """Generates tree node with type and status"""
    first_value = first_dict.get(key)
    second_value = second_dict.get(key)
    if first_value is None:
        node = {
            'status': ADDED,
            'value': second_value
        }
    elif second_value is None:
        node = {
            'status': REMOVED,
            'value': first_value
        }
    elif isinstance(first_value, dict) and isinstance(second_value, dict):
        node = {
            'status': NESTED,
            'value': compare_dicts(first_value, second_value)
        }
    elif first_value == second_value:
        node = {
            'status': UNCHANGED,
            'value': first_value
        }
    else:
        node = {
            'status': CHANGED,
            'first_value': first_value,
            'second_value': second_value
        }
    return node
