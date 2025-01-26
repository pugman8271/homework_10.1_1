from src import masks

user_input_card = input("Введите номер карты: ")
user_input_mask = input("Введите номер счета: ")
print(masks.get_mask_card_number(user_input_card))
print(masks.get_mask_account(user_input_mask))
