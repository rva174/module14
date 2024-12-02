from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
#from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import os



from grud_function import *
from add_products import *


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_catalog = KeyboardButton(text='Перейти в каталог продуктов')
button_about = KeyboardButton(text='О нас')
button_reg = KeyboardButton(text='Регистрация')

kb.add(button_catalog, button_about)
kb.add(button_reg)



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Мы продаем продукты для Вашего здоровья:", reply_markup=kb)


@dp.message_handler(text='Перейти в каталог продуктов')
async def get_buying_list(message: types.Message):
    products = get_all_products(db_name="database.db")

    if products:
        for product in products:
            title, description, price = product[1], product[2], product[3]

            # Отправка фото если оно есть
            photo_path = os.path.join('files', f"{title.lower()}.jpg")  # Используем название товара

            if os.path.exists(photo_path):
                await bot.send_photo(
                    chat_id=message.chat.id,
                    photo=open(photo_path, 'rb'),
                    caption=f"Название: {title}\nОписание: {description}\nЦена: {price}"
                )
            else:
                await message.answer(f"Название: {title}\nОписание: {description}\nЦена: {price}\n(Фото нет)")

        await message.answer("Чтобы вернуться в меню, воспользуйтесь кнопками ниже:",
                             reply_markup=kb)  # Возвращаем клавиатуру после списка продуктов
    else:
        await message.reply("Нет доступных продуктов.",
                            reply_markup=kb)  # Также возвращаем клавиатуру, если нет продуктов

@dp.message_handler(text='О нас')
async def inform_about_us(message):
    await message.answer('Мы продаем только натуральные продукты')


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text):
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    username, email, age = data['username'], data['email'], data['age']
    add_user(username, email, age)
    await message.answer('Регистрация проведена успешно!', reply_markup=kb)
    await state.finish()

@dp.message_handler()  # Общий обработчик
async def all_message(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)