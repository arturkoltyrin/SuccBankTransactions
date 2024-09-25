from typing import List, Dict


def filter_by_state(data: List[Dict[str, str]], state: str = 'EXECUTED') -> List[Dict[str, str]]:
    """Фильтрует список словарей по заданному состоянию.
    Args:
        data (List[Dict[str, str]]): Список словарей, содержащих данные.
        state (str): Состояние, по которому будет происходить фильтрация.
                     По умолчанию 'EXECUTED'.
    Returns:
        List[Dict[str, str]]: Новый список словарей, содержащих только те элементы,
                               которые имеют указанное состояние."""

    return [i for i in data if i.get('state') == state]


def sort_by_date(data: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    """Сортирует список словарей по дате.
    Args:
        data (List[Dict[str, str]]): Список словарей, содержащих данные.
        reverse (bool): Если True, сортирует в обратном порядке. По умолчанию False.
    Returns:
        List[Dict[str, str]]: Новый отсортированный список словарей по дате."""

    return sorted(data, key=lambda x: x.get('date'), reverse=reverse)
