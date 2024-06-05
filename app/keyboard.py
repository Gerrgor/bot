from aiogram.types import ReplyKeyboardMarkup
from app.config import KB

# Все виды F4
my_keyboard_1 = ReplyKeyboardMarkup(
    keyboard=[[KB.button_5, KB.button_6], [KB.button_7], [KB.button_10]],
    resize_keyboard=True,
)

# Все виды наработанного F4D
my_keyboard_2 = ReplyKeyboardMarkup(
    keyboard=[[KB.button_5, KB.button_6], [KB.button_17], [KB.button_10]],
    resize_keyboard=True,
)

# Все виды PPA
my_keyboard_3 = ReplyKeyboardMarkup(
    keyboard=[[KB.button_8, KB.button_9], [KB.button_10]], resize_keyboard=True
)

# Взятие/наработка
my_keyboard_4 = ReplyKeyboardMarkup(
    keyboard=[[KB.button_11, KB.button_12], [KB.button_10]], resize_keyboard=True
)

# Виды порошка
my_keyboard_5 = ReplyKeyboardMarkup(
    keyboard=[[KB.button_1, KB.button_2], [KB.button_10]], resize_keyboard=True
)

# Виды процесса
my_keyboard_6 = ReplyKeyboardMarkup(
    keyboard=[[KB.button_15, KB.button_16]], resize_keyboard=True
)

# Вещества на суспензию
my_keyboard_7 = ReplyKeyboardMarkup(
    keyboard=[[KB.button_1, KB.button_3], [KB.button_13, KB.button_14], [KB.button_10]],
    resize_keyboard=True,
)
my_keyboard_8 = ReplyKeyboardMarkup(keyboard=[[KB.button_18, KB.button_10]], resize_keyboard=True
)