from aiogram import Bot
from aiogram.types import BotCommand
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import KeyboardButton


async def set_main_menu(bot: Bot):

    main_menu_commands = [
        BotCommand(command="/start", description="Начало работы"),
        BotCommand(command="/help", description="Справка по работе бота"),
        BotCommand(command="/support", description="Поддержка"),
    ]

    await bot.set_my_commands(main_menu_commands)


class DiffStates(StatesGroup):
    F4 = State()
    F4D = State()
    PPA = State()
    Spirt = State()
    Talc = State()
    PEG = State()
    _0460 = State()
    _0490 = State()
    MP = State()
    MPX = State()
    VRX = State()
    Taken = State()
    Accumulated = State()
    Mill = State()
    Dryer = State()
    Taken_Mill = State()
    Taken_Dryer = State()
    Accumulated_Mill = State()
    Cyclone = State()


class KB:
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
    button_15 = KeyboardButton(text="Мельница")
    button_16 = KeyboardButton(text="Сушка")
    button_17 = KeyboardButton(text="Циклон")
    button_18 = KeyboardButton(text='Правильно')
