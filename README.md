# SuccBankTransactions

## Описание проекта

SuccBankTransactions - это проект, разработанный на Python для маскировки номеров банковских карт и счетов.

## Установка

Чтобы установить и использовать проект, выполните следующие шаги:

1. **Клонирование репозитория**

git clone https://github.com/arturkoltyrin/SuccBankTransactions.git

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

print(masked_card) 

Вывод: XXXX XX90 **** 6361

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

print(masked_account_info) 

Вывод: **8305

**`get_date(date_str: str)`**

Преобразует строку с датой в формат `DD.MM.YYYY`.

**Пример использования:**

from src.widget import get_date

formatted_date = get_date("2024-03-11T02:26:18.671407")

print(formatted_date)

Вывод: 11.03.2024

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

print(sorted_transactions)

Вывод: [{'date': '2024-03-10', 'amount': 50}]

### Модуль `generators`

#### Функции:

**`filter_by_currency(transactions, currency)`**

Функция фильтрует транзакции по заданной валюте и возвращает итератор.

**Параметры:**
- `transactions` (list): Список транзакций.
- `currency` (str): Код валюты для фильтрации.

**Пример использования:**

usd_transactions = filter_by_currency(transactions, "USD")

for transaction in usd_transactions:

print(transaction)

**`transaction_descriptions(transactions)`**

Генератор, который возвращает описание каждой операции по очереди.

**Параметры:**
- `transactions` (list): Список транзакций.

**Пример использования:**

descriptions = transaction_descriptions(transactions)

for description in descriptions:

print(description)

**`card_number_generator(start, end)`**

Генератор, который выдает номера карт в формате XXXX XXXX XXXX XXXX.

**Параметры:**
- `start` (int): Начальное значение диапазона.
- `end` (int): Конечное значение диапазона (включительно).

**Пример использования:**

for card_number in card_number_generator(1, 5):

print(card_number)

### Модуль `decorators`

Модуль содержит декоратор `log`, который используется для логирования выполнения функций, включая сообщения об их запуске, успешном завершении и возникающих ошибках.
Декоратор может выводить логи в консоль или записывать их в файл.

#### Функции:

**`def log(filename: Optional[str] = None) -> Callable:`**
Декоратор для логирования функций.

Логирует начало, конец выполнения функции и ее результаты и ошибки

**Пример использования:**

from decorators import log

@log()

def add(a, b):

return a + b

@log()

def divide(a, b):

return a / b

result = add(3, 4) # Запись в консоль: "Запуск функции 'add' с параметрами: (3, 4), {}"

result = divide(10, 2) # Запись в консоль: "Запуск функции 'divide' с параметрами: (10, 2), {}"

Логирование в файл

Если хотите записывать логи в файл, передайте имя файла в качестве аргумента:

@log("file.txt")

def multiply(a, b):

return a * b

### Модуль `external_api`
#### Функции:

**`convert_to_rub(transaction: dict) -> float`**

Функция конвертирует сумму транзакции из заданной валюты в рубли (RUB).

Параметры:
- transaction (dict): Словарь, содержащий данные транзакции, включая сумму и валюту.

Возвращает:
- float: Сумма в рублях.

**Пример использования:**

transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
rub_amount = convert_to_rub(transaction)
print(rub_amount)

### Модуль `utils`
#### Функции:

**`load_transactions(filepath: str) -> List[Dict[str, Any]]`**

Функция загружает финансовые транзакции из JSON-файла.

Параметры:
- filepath (str): Путь к JSON-файлу с транзакциями.

Возвращает:
- List[Dict[str, Any]]: Список транзакций в виде словарей. Если файл не найден или содержит ошибку, возвращает пустой список.

**Пример использования:**

transactions = load_transactions("transactions.json")
print(transactions)

## Тестирование модулей

В проекте реализованы тесты для проверок функций, 
связанных с обработкой и форматированием данных. 
Все тесты написаны с использованием библиотеки `pytest`.

### Тестируемые функции

### 1. `get_date`
Функция `get_date` преобразует дату из строкового формата 
в более удобный вид (формат `DD.MM.YYYY`).

#### Тесты:
- Входные данные: `"2024-03-11T02:26:18.671407"` → Ожидаемый результат: `"11.03.2024"`
- Входные данные: `"2023-01-01T02:26:18.671407"` → Ожидаемый результат: `"01.01.2023"`
- Некорректный ввод (пустая строка) вызывает исключение `ValueError` 
с сообщением "Данные отсутствуют".

### 2. `mask_account_card`
Функция `mask_account_card` маскирует номера банковских карт и счетов, 
оставляя только последние 4 цифры.

#### Тесты:
- Входные данные: `"Maestro 1596837868705199"` → Ожидаемый результат: `"Maestro 1596 83** **** 5199"`
- Входные данные: `"Счет 64686473678894779589"` → Ожидаемый результат: `"Счет **9589"`
- Входные данные: `"MasterCard 7158300734726758"` → Ожидаемый результат: `"MasterCard 7158 30** **** 6758"`
- Также тестируются другие типы карт и счетов с аналогичными ожиданиями.

### 3. `get_mask_card_number`
Функция `get_mask_card_number` возвращает замаскированный номер карты, 
оставляя только последние 4 цифры.

#### Тесты:
- Входные данные: `"Maestro 1596837868705199"` → Ожидаемый результат: `"1596 83** **** 5199"`
- Входные данные: `"Счет 64686473678894779589"` → Ожидаемый результат: `"**9589"`
- При неверном вводе (например, отсутствие названия или номера) 
вызывается `ValueError`.

### 4. `get_mask_account`
Функция `get_mask_account` маскирует номера счетов, оставляя только последние 4 цифры.

#### Тесты:
- Входные данные: `"73654108430135874305"` → Ожидаемый результат: `"**4305"`
- Входные данные: `"84930254671289437564"` → Ожидаемый результат: `"**7564"`
- Тестируются и другие номера счетов.

### 5. `filter_by_state`
Функция `filter_by_state` фильтрует список словарей по заданному состоянию (`state`).

#### Тесты:
- Входные данные: список с состояниями `["EXECUTED", "CANCELED"]`
→ Ожидаемый результат: `[{ "state": "EXECUTED", "amount": 100 }, { "state": "EXECUTED", "amount": 300 }]`
- При фильтрации по несуществующему состоянию возвращается пустой список.

### 6. `sort_by_date`
Функция `sort_by_date` сортирует список словарей по дате.

#### Тесты:
- Входные данные с датами в различном порядке → Сортировка по возрастанию и убыванию дате.
- Проверяется, что данные правильно сортируются в соответствии с заданным параметром `reverse`.

### 7. `filter_by_currency(transactions, currency)`
Функция фильтрует транзакции по заданной валюте и возвращает итератор.

#### Тесты:
- **Сценарий 1:** Входные данные с транзакциями в различных валютах → Проверка, что функция возвращает только транзакции с нужной валютой.
  - Проверяется, что для валюты "USD" возвращаются только соответствующие транзакции.
  
- **Сценарий 2:** Отсутствие транзакций с заданной валютой → Проверка, что функция возвращает пустой список, если валюты нет.
  - Проверка для несуществующей валюты, например, "JPY".

- **Сценарий 3:** Пустой список транзакций → Проверка, что функция также возвращает пустой список при передаче пустого списка.

### 8. `transaction_descriptions(transactions)`
Генератор, который возвращает описание каждой операции по очереди.

#### Тесты:
- **Сценарий 1:** Входные данные с несколькими транзакциями → Проверка, что функция возвращает корректные описания всех транзакций.
  - Проверяется соответствие описаний возвращаемых транзакций с ожидаемыми.

- **Сценарий 2:** Пустой список транзакций → Проверка, что функция возвращает пустой список при отсутствии транзакций.
  - Генератор корректно работает без ошибок при пустом списке.

### 9. `card_number_generator(start, end)`
Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.

#### Тесты:

- **Сценарий 1:** Генерация номеров в стандартном диапазоне → Проверка, что функция выдает правильные номера от 1 до 5.
  - Каждый сгенерированный номер соответствует формату 16 цифр с пробелами.

- **Сценарий 2:** Пустой диапазон (начальное значение больше конечного) → Проверка, что функция возвращает пустой список.
  - Проверка случая, когда начальное значение больше конечного, например, от 5 до 1.

- **Сценарий 3:** Граничные значения диапазона → Проверка, что функция корректно обрабатывает, когда диапазон содержит одно значение.
  - Проверка генерации только одного номера карты при совпадении начального и конечного значений.

### 10. `@log()`
Декоратор `log`, который используется для логирования выполнения функций, включая сообщения об их запуске, успешном завершении и возникающих ошибках. Декоратор может выводить логи в консоль или записывать их в файл.

#### Тесты:

- **Сценарий 1:** Успешное выполнение функции сложения → Проверка, что функция `add` возвращает правильный результат при добавлении двух чисел.
  - Входные параметры: `3` и `4`. Ожидается результат `7`.
  - Логирование должно содержать сообщения о запуске функции и успешном выполнении.

- **Сценарий 2:** Деление на ноль → Проверка, что функция `divide` обрабатывает исключение `ZeroDivisionError`.
  - Входные параметры: `10` и `0`. Ожидается, что будет вызвано исключение.
  - Логирование должно содержать сообщение об ошибке и входных параметрах.

- **Сценарий 3:** Генерация исключения → Проверка, что функция `raise_exception` генерирует `ValueError`.
  - Ожидается, что будет вызвано исключение с сообщением "Some error occurred".
  - Логирование должно содержать сообщение об ошибке и входных параметрах.

### 11. `convert_to_rub(transaction: dict) -> float`
Генератор, который конвертирует сумму транзакции из заданной валюты в рубли (RUB).

##### Тесты:
- **Сценарий 1:** Валюта транзакции в рублях.
  - Проверка, что функция возвращает правильное значение (150.0 RUB).

- **Сценарий 2:** Успешная конвертация из USD в RUB.
  - Проверка, что функция возвращает корректный результат (12000.0 RUB).

- **Сценарий 3:** Ошибка при запросе на API.
  - Проверка обработки ошибки, возвращающей 0.0.

- **Сценарий 4:** Некорректный ответ от API.
  - Проверка того, что функция возвращает 0.0 в случае некорректного ответа.

### 12. `load_transactions(filepath: str) -> List[Dict[str, Any]]`
Функция, загружающая финансовые транзакции из JSON-файла.

##### Тесты:
- **Сценарий 1:** Файл не существует.
  - Проверка, что функция возвращает пустой список при отсутствии файла.

- **Сценарий 2:** Путь не является файлом.
  - Проверка, что функция возвращает пустой список, если путь не файл.

- **Сценарий 3:** Пустой файл.
  - Проверка, что функция возвращает пустой список при загрузке из пустого файла.

- **Сценарий 4:** Корректный JSON-файл.
  - Проверка, что функция возвращает ожидаемые транзакции из правильного файла.

- **Сценарий 5:** Некорректный JSON.
  - Проверка обработки ошибок при загрузке из файла с некорректным JSON, возвращающего пустой список.

### Запуск тестов

Для выполнения тестов необходимо иметь установленный `pytest`. 
Можно запустить тесты с помощью команды  `pytest`.

## Проверка качества кода

Проект использует следующие инструменты:

- **Flake8** для проверки стиля кода.
- **Black** для автоматического форматирования кода.
- **isort** для упорядочивания импортов.
- **Mypy** для статической проверки типов.

## Лицензия

Этот проект лицензирован под MIT License.