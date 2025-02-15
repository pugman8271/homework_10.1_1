def filter_by_currency(transactions, currency="USD"):

    for transaction in transactions:
        if (
            transaction.get("operationAmount", {}).get("currency", {}).get("code")
            == currency
        ):
            yield transaction


def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start, stop):
    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"


for card_number in card_number_generator(0, 5):
    print(card_number)
