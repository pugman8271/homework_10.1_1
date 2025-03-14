from src.processing import (
    filter_by_state,
    sort_by_category,
    sort_by_currency,
    sort_by_date,
    sort_by_keyword,
    sorting_by_amount,
)
from src.transactions_reader import transactions_reader_csv, transactions_reader_xlsx
from src.utils import operations_json_get_info
from src.widget import get_date, mask_account_card


def main() -> None:

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    user_choice = input(
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
    )
    if user_choice == "1":
        print("Для обработки выбран JSON-файл.")
        directory_to_file = "data/operations.json"
        opener = operations_json_get_info
    elif user_choice == "2":
        print("Для обработки выбран CSV-файл.")
        directory_to_file = "transactions.csv"
        opener = transactions_reader_csv
    elif user_choice == "3":
        print("Для обработки выбран XLSX-файл.")
        directory_to_file = "transactions_excel.xlsx"
        opener = transactions_reader_xlsx
    else:
        print("Путь не выбран")

    operation_list = opener(directory_to_file)

    while True:
        user_choice_status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        )
        user_choice_status = user_choice_status.upper()
        if user_choice_status not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции {user_choice_status} недоступен.")
        else:
            print(f"Операции отфильтрованы по статусу {user_choice_status}")
            operation_list = filter_by_state(operation_list, user_choice_status)

        # Сортировка по дате
        sorting_by_date = (input("Отсортировать операции по дате? Да/Нет\n")).lower()
        if sorting_by_date == "да":
            # Сортировка от новых к старым
            sorting_by_date = True
            operation_list = sort_by_date(operation_list, sorting_by_date)
        else:
            # Сортировка от старых к новым
            sorting_by_date = False
            operation_list = sort_by_date(operation_list, sorting_by_date)

        # Сортировка по возрастанию
        sorting_by_increasing = (
            input("Отсортировать по возрастанию или по убыванию?\n")
        ).lower()
        if sorting_by_increasing == "по возрастанию":
            # От большего к меньшему
            sorting_by_increasing = False
            operation_list = sorting_by_amount(operation_list, sorting_by_increasing)
        else:
            # От меньшего к большему
            sorting_by_increasing = True
            operation_list = sorting_by_amount(operation_list, sorting_by_increasing)

        # Сортировка по валюте
        sorting_by_currency = (
            input("Выводить только рублевые тразакции? Да/Нет\n")
        ).lower()
        if sorting_by_currency == "да":
            operation_list = sort_by_currency(operation_list)

        # Сортировка по описанию
        sorting_by_description = (
            input(
                "Отфильтровать список транзакций "
                "по определенному слову в описании? Да/Нет\n"
            )
        ).lower()
        if sorting_by_description == "да":
            user_filter_description = input(
                "Введите слово, по которому необходимо найти оперции\n"
            )
            operation_list = sort_by_keyword(operation_list, user_filter_description)
        else:
            operation_list = operation_list

            print("Распечатываю итоговый список транзакций...")
            print(
                f"Всего банковских операций в выборке: "
                f"{sum(v for k, v in (sort_by_category(operation_list).items()))}"
            )
            for operation in operation_list:
                # print(operation["description"])
                # print(get_date(str(operation["date"])))
                # print(mask_account_card(str(operation["from"])))
                # print(mask_account_card(str(operation["to"])))
                # print((operation["operationAmount"]["amount"]), (operation["operationAmount"]["currency"]["code"]))
                # print((operation['amount']), (operation['currency_code']))

                print(operation["description"])
                if "date" in operation and not None:
                    print(get_date(str(operation["date"])))
                if "from" in operation and not None:
                    print(mask_account_card(str(operation["from"])))
                if "to" in operation and not None:
                    print(mask_account_card(str(operation["to"])))
                if "operationAmount" in operation:
                    print(
                        (operation["operationAmount"]["amount"]),
                        (operation["operationAmount"]["currency"]["code"]),
                    )
                if "amount" in operation:
                    print((operation["amount"]), (operation["currency_code"]))
                    print("********************************************")
        break


main()
