import json
import pandas as pd
import logging
from datetime import datetime
from functools import wraps
from typing import Optional

logger = logging.getLogger("main.reports")
logger.setLevel(logging.DEBUG)


def log_report(func):
    """Декоратор для записи отчета в файл."""

    @wraps(func)
    def wrapper(*args, kwargs):
        result = func(*args, kwargs)

        filename = f"report_{func.__name__}_{datetime.now().strftime('%Y%m%d')}.json"
        with open(filename, 'w') as f:
            json.dump(result, f, ensure_ascii=False)
        logger.info(f"Отчет записан в {filename}.")
        return result

    return wrapper


@log_report
def spending_by_weekday(transactions: pd.DataFrame, date: Optional[str] = None) -> pd.DataFrame:
    """Возвращает средние траты по дням недели за последние 3 месяца."""
    if date is None:
        date = datetime.now()
    else:
        date = pd.to_datetime(date)

    three_months_ago = date - pd.DateOffset(months=3)
    transactions['date'] = pd.to_datetime(transactions['date'])
    filtered_transactions = transactions[
        (transactions['date'] >= three_months_ago) &
        (transactions['date'] <= date)]

    filtered_transactions['weekday'] = filtered_transactions['date'].dt.day_name()
    average_spending = filtered_transactions.groupby('weekday')['amount'].mean().reset_index()
    logger.debug("Average spending by weekday calculated.")

    return average_spending
