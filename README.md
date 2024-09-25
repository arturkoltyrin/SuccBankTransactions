# SuccBankTransactions

## Описание проекта

SuccBankTransactions - это проект, разработанный на Python для маскировки номеров банковских карт и счетов.

## Установка

Чтобы установить и использовать проект, выполните следующие шаги:

1. **Клонирование репозитория**

'''
git clone https://github.com/arturkoltyrin/SuccBankTransactions.git
'''

2. **Установка зависимостей**

Убедитесь, что у вас установлен Poetry.

Затем выполните команду: poetry install

3. **Запуск проекта**

Вы можете запустить проект и использовать его функции
в интерактивной оболочке, используя:
   
poetry run python

## Использование

Проект содержит несколько модулей:

### Модуль `masks`

#### Функции:

**`get_mask_card_number(card_number: str)`**

Маскирует номер банковской карты. 
Возвращает строку в формате `XXXX XX** **** XXXX`, где X – цифры карты.

**Пример использования:**
  
from src.masks import get_mask_card_number

masked_card = get_mask_card_number("7000792289606361")
print(masked_card) # Вывод: XXXX XX90 **** 6361

**`get_mask_account(account_number: str)`**

Маскирует номер банковского счета.
Возвращает строку в формате `**XXXX`, где X – цифры счета.

**Пример использования:**

from src.masks import get_mask_account

masked_account = get_mask_account("73654108430135874305")
print(masked_account) # Вывод: **8305

### Модуль `widget`

#### Функции:

**`mask_account_card(info: str)`**

Маскирует номер карты или счета в зависимости
от указанного типа (карта или счет). 
Принимает строку, содержащую тип и номер.

**Пример использования:**

from src.widget import mask_account_card

masked_info = mask_account_card("Visa Platinum 7000792289606361")
print(masked_info) # Вывод: XXXX XX90 **** 6361

masked_account_info = mask_account_card("Счет 73654108430135874305")
print(masked_account_info) # Вывод: **8305

**`get_date(date_str: str)`**

Преобразует строку с датой в формат `DD.MM.YYYY`.

**Пример использования:**

from src.widget import get_date

formatted_date = get_date("2024-03-11T02:26:18.671407")
print(formatted_date) # Вывод: 11.03.2024

### Модуль `processing`

#### Функции:

**`filter_by_state(transactions: List[Dict], state: str = 'EXECUTED')`**

Фильтрует транзакции по состоянию. 
Возвращает только те транзакции, 
у которых состояние соответствует указанному значению.

**Пример использования:**

from src.processing import filter_by_state

transactions = [{'state': 'EXECUTED', 'amount': 100}]
executed_transactions = filter_by_state(transactions)
print(executed_transactions) # Вывод: [{'state': 'EXECUTED', 'amount': 100}]

**`sort_by_date(transactions: List[Dict], order: str = 'desc')`**

Сортирует транзакции по дате. Поддерживает сортировку по возрастанию и убыванию.

**Пример использования:**

from src.processing import sort_by_date

transactions = [{'date': '2024-03-11', 'amount': 100}]
sorted_transactions = sort_by_date(transactions, order='asc')
print(sorted_transactions) # Вывод: [{'date': '2024-03-10', 'amount': 50}]

## Проверка качества кода

Проект использует следующие инструменты:

- **Flake8** для проверки стиля кода.
- **Black** для автоматического форматирования кода.
- **isort** для упорядочивания импортов.
- **Mypy** для статической проверки типов.

## Лицензия

Этот проект лицензирован под MIT License.