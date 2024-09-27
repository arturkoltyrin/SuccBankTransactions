from typing import List, Dict


def filter_by_state(data: List[Dict[str, str]], state: str = 'EXECUTED') -> List[Dict[str, str]]:
    """ Создает новый список словарей, содержащий только те словари,
        у которых ключ 'state' соответствует заданному значению."""

    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict[str, str]], reverse: bool = False) -> List[Dict[str, str]]:
    """Создает новый список, отсортированный по дате в указанном порядке."""

    return sorted(data, key=lambda x: x.get('date'), reverse=reverse)
