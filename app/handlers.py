from aiogram import Router, F
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from app import keyboard
from program import Env
from app.message import AKCBD

storage = MemoryStorage()
akc = AKCBD()
router = Router()


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


keys = ["state1", "state2", "comment", "table"]
states = dict.fromkeys(keys)
# keys2 = []
# data = dict.fromkeys(keys2)

env = Env()
env.read_env()


@router.message(F.text == "Назад")
@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await message.answer(
        text="Привет. Выберите заносимые данные", reply_markup=keyboard.my_keyboard_5
    )
    await state.clear()


@router.message(F.text == "Взятое")
async def process_taken_command(message: Message, state: FSMContext):
    await message.answer(text="Выберите продукт", reply_markup=keyboard.my_keyboard_1)
    await state.set_state(DiffStates.Taken)
    states["table"] = "Взятое"


@router.message(F.text == "Наработанное")
async def process_accumulated_command(message: Message, state: FSMContext):
    await message.answer(text="Выберите продукт", reply_markup=keyboard.my_keyboard_6)
    await state.set_state(DiffStates.Accumulated)
    states["table"] = "Наработанное"


# F4
@router.message(F.text == "F4")
async def process_f4_command(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите взятый продукт", reply_markup=keyboard.my_keyboard_2
    )
    await state.set_state(DiffStates.F4)
    await state.update_data(state1="F4")


# F4D
@router.message(F.text == "F4D")
async def process_f4d_command(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите взятый продукт", reply_markup=keyboard.my_keyboard_3
    )
    await state.set_state(DiffStates.F4D)
    await state.update_data(state1="F4D")


# PPA
@router.message(F.text == "PPA")
async def process_ppa_command(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите взятый продукт", reply_markup=keyboard.my_keyboard_4
    )
    await state.set_state(DiffStates.PPA)
    await state.update_data(state1="PPA")


# 0460/0490
@router.message(F.text == "0460")
async def process_0460_command(message: Message, state: FSMContext):
    await message.answer(text="Введите количество", reply_markup=ReplyKeyboardRemove())
    await state.set_state(DiffStates._0460)
    await state.update_data(state2="0460")


@router.message(F.text == "0490")
async def process_0490_command(message: Message, state: FSMContext):
    await message.answer(text="Введите количество", reply_markup=ReplyKeyboardRemove())
    await state.set_state(DiffStates._0490)
    await state.update_data(state2="0490")


# Спирт
@router.message(F.text == "Спирт")
async def process_spirt_command(message: Message, state: FSMContext):
    await message.answer(text="Введите количество", reply_markup=ReplyKeyboardRemove())
    await state.set_state(DiffStates.Spirt)
    await state.update_data(state2="Спирт")


@router.message(F.text == "PEG")
async def process_peg_command(message: Message, state: FSMContext):
    await message.answer(text="Введите количество", reply_markup=ReplyKeyboardRemove())
    await state.set_state(DiffStates.PEG)
    await state.update_data(state2="PEG")


@router.message(F.text == "Тальк")
async def process_talc_command(message: Message, state: FSMContext):
    await message.answer(text="Введите количество", reply_markup=ReplyKeyboardRemove())
    await state.set_state(DiffStates.Talc)
    await state.update_data(state2="Тальк")


# MP/MPX/VRX
@router.message(F.text == "MP")
async def process_mp_command(message: Message, state: FSMContext):
    await message.answer(text="Введите количество", reply_markup=ReplyKeyboardRemove())
    await state.set_state(DiffStates.MP)
    await state.update_data(state2="MP")


@router.message(F.text == "MPX")
async def process_mpx_command(message: Message, state: FSMContext):
    await message.answer(text="Введите количество", reply_markup=ReplyKeyboardRemove())
    await state.set_state(DiffStates.MPX)
    await state.update_data(state2="MPX")


@router.message(F.text == "VRX")
async def process_vrx_command(message: Message, state: FSMContext):
    await message.answer(text="Введите количество", reply_markup=ReplyKeyboardRemove())
    await state.set_state(DiffStates.VRX)
    await state.update_data(state2="VRX")


# Ввод количества
@router.message(StateFilter(DiffStates.MPX))
@router.message(StateFilter(DiffStates.MP))
@router.message(StateFilter(DiffStates.VRX))
@router.message(StateFilter(DiffStates._0460))
@router.message(StateFilter(DiffStates._0490))
@router.message(StateFilter(DiffStates.Spirt))
@router.message(StateFilter(DiffStates.PEG))
@router.message(StateFilter(DiffStates.Talc))
async def process_comment_command(message: Message, state: FSMContext):
    username = message.from_user.username  # type: ignore
    date_time = message.date.now().strftime("%d/%m/%Y, %H:%M:%S")
    states["state2"] = await state.get_data()
    product = "".join(states["state2"].values())
    await state.clear()
    await state.update_data(comment=message.text)
    states["comment"] = await state.get_data()
    comment = message.text
    await message.answer(text="Спасибо! К началу /start")
    if states["table"] == "Взятое":
        return akc.taken(
            username=username, date_time=date_time, product=product, comment=comment
        )
    elif states["table"] == "Наработанное":
        return akc.accumulated(
            username=username, date_time=date_time, product=product, comment=comment
        )


@router.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(
        text="В случае возникновения ошибок в работе бота /support , /start из любого места вернет к началу работы бота"
    )


@router.message(Command(commands="support"))
async def process_support_command(message: Message):
    await message.answer_contact(phone_number=env("p_n"), first_name=env("f_n"))


@router.message()
async def process_trash_command(message: Message):
    await message.answer(text="Я Вас не понимаю")
