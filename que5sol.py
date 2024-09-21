"""
Python function aggregate_data(data: List[Dict], key: str,
aggregator: Callable) that aggregates values from a list of
dictionaries. The function should group the dictionaries by the
provided key and apply the aggregator function to the grouped
values
"""
from typing import List, Dict, Callable

def aggregate_data(data: List[Dict], key: str, aggregator: Callable):
    """
    function aggregate_data(data: List[Dict], key: str,
    aggregator: Callable) that aggregates values from a list of
    dictionaries.
    :param data: Object of the input list
    :param key: key variable
    :param aggregator: aggregator function
    :return: aggregated result
    """
    grouped_data = {}

    for item in data:
        group_key = item[key]
        if group_key not in grouped_data:
            grouped_data[group_key] = []
        grouped_data[group_key].append(item)

    aggregated_result = {}
    for group_key, group_values in grouped_data.items():
        aggregated_result[group_key] = aggregator(group_values)

    return aggregated_result

# Example usage:
data = [
    {"category": "fruit", "value": 10},
    {"category": "vegetable", "value": 20},
    {"category": "fruit", "value": 15},
    {"category": "fruit", "value": 5},
    {"category": "vegetable", "value": 30},
]

def sum_aggregator(group):
    """
    Aggregator function: sum values of each group
    :param group: object of group list
    :return: sum of the respective category values
    """
    return sum(item['value'] for item in group)


# Aggregate data by category, summing the values in each group
result = aggregate_data(data, "category", sum_aggregator)
print(result)
