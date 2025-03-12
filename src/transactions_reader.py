import csv

import pandas as pd


def transactions_reader_csv(directory):
    """Функция чтения csv файлов"""
    with open(directory, encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        return list(reader)


def transactions_reader_xlsx(directory):
    """Функция чтения excel файлов"""
    reader_xlsx = pd.read_excel(directory)
    return reader_xlsx.to_dict(orient="records")


