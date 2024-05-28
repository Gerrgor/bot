from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
)

button_1 = KeyboardButton(text="F4")
button_2 = KeyboardButton(text="F4D")
button_3 = KeyboardButton(text="Спирт")
button_4 = KeyboardButton(text="PPA")
button_5 = KeyboardButton(text="MP")
button_6 = KeyboardButton(text="MPX")
button_7 = KeyboardButton(text="VRX")
button_8 = KeyboardButton(text="0460")
button_9 = KeyboardButton(text="0490")
button_10 = KeyboardButton(text="Назад")
button_11 = KeyboardButton(text="Взятое")
button_12 = KeyboardButton(text="Наработанное")
button_13 = KeyboardButton(text="PEG")
button_14 = KeyboardButton(text="Тальк")

my_keyboard_1 = ReplyKeyboardMarkup(
    keyboard=[
        [button_1, button_2],
        [button_3, button_4],
        [button_13, button_14],
        [button_10],
    ],
    resize_keyboard=True,
)
my_keyboard_2 = ReplyKeyboardMarkup(
    keyboard=[[button_5, button_6, button_7], [button_10]], resize_keyboard=True
)
my_keyboard_3 = ReplyKeyboardMarkup(
    keyboard=[[button_5, button_6], [button_10]], resize_keyboard=True
)
my_keyboard_4 = ReplyKeyboardMarkup(
    keyboard=[[button_8, button_9], [button_10]], resize_keyboard=True
)
my_keyboard_5 = ReplyKeyboardMarkup(
    keyboard=[[button_11, button_12]], resize_keyboard=True
)
my_keyboard_6 = ReplyKeyboardMarkup(
    keyboard=[[button_1, button_2], [button_4], [button_10]], resize_keyboard=True
)
