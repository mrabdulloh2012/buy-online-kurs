from aiogram import Dispatcher, Bot , filters, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from aiogram.fsm.state import State , StatesGroup
from aiogram.fsm.context import FSMContext
import openai


SECRET_KEY = "sk-proj-cuIY2hWHGQxoJYrNNteXT3BlbkFJyXE1MtMjr9GWsPY3AEuT"
openai.api_key = SECRET_KEY


bot = Bot(token='7304738402:AAFf9cGQL5yKGGsere7j-fM1LcGsyAkU-pU')
dp = Dispatcher(bot = bot)

class Registration_rus(StatesGroup):
    first_name = State()
    last_name = State()
    number = State()
    

class Registration_uzb(StatesGroup):
    first_name = State()
    last_name = State()
    number = State()
    
    
class Cart(StatesGroup):
    cart_number = State()
    
class Cart_ru(StatesGroup):
    cart_number = State()
    
    
    
    
    
    
contact_button = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Kontakt jo'natish", request_contact=True)]
], resize_keyboard=True)



contact_button_rus = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Отправить контакт", request_contact=True)]
], resize_keyboard=True)
    
    
    
    
    
start_language_keyboard = [
    [KeyboardButton(text='uzb 🇺🇿'),KeyboardButton(text='rus 🇺🇿')]
]

start_language_button = ReplyKeyboardMarkup(keyboard=start_language_keyboard,resize_keyboard=True)    


 








big_menu_keyboard_uzb = [
    [KeyboardButton(text='kurslar 🔖'),KeyboardButton(text='korzinka 🛒'),KeyboardButton(text='yordam 🆘')],
    [KeyboardButton(text='biz haqida 👈'),KeyboardButton(text='til 🇷🇺🔄🇺🇿')]
]

big_menu_button_uzb = ReplyKeyboardMarkup(keyboard=big_menu_keyboard_uzb,resize_keyboard=True)    


big_menu_keyboard_rus = [
    [KeyboardButton(text='курсы 🔖'),KeyboardButton(text='корзина 🛒'),KeyboardButton(text='помощь 🆘')],
    [KeyboardButton(text='О нас 👈'),KeyboardButton(text='язык 🇷🇺🔄🇺🇿')]
]

big_menu_button_rus = ReplyKeyboardMarkup(keyboard=big_menu_keyboard_rus,resize_keyboard=True)  
    
    
    
menu_kurs_keyboard_rus = [
    [KeyboardButton(text='баккенд'),KeyboardButton(text='фронт энд'),KeyboardButton(text='дизайн')],
    [KeyboardButton(text='стартер'),KeyboardButton(text='основы git'),KeyboardButton(text='Мой первый шаг в ит')],
    [KeyboardButton(text='назад ⬅️')]
]

menu_kurs_button_rus = ReplyKeyboardMarkup(keyboard=menu_kurs_keyboard_rus,resize_keyboard=True)    


menu_kurs_keyboard_uzb = [
    [KeyboardButton(text='backend'),KeyboardButton(text='front-end'),KeyboardButton(text='dizine')],
    [KeyboardButton(text='starter'),KeyboardButton(text='git asoslari'),KeyboardButton(text='It sohasiga ilk qandam')],
    [KeyboardButton(text='ortga ⬅️')]
]

menu_kurs_button_uzb = ReplyKeyboardMarkup(keyboard=menu_kurs_keyboard_uzb,resize_keyboard=True)    
    
    
    
    
buy_backend_keyboard_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒",callback_data="buy backend"),InlineKeyboardButton(text="🚫",callback_data="imkor qilish")]
    
]) 

buy_front_end_keybaord_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒",callback_data="buy front-end"),InlineKeyboardButton(text="🚫",callback_data="imkor qilish")]
    
]) 

buy_dizene_keyboard_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒",callback_data="buy dizine"),InlineKeyboardButton(text="🚫",callback_data="imkor qilish")]
    
]) 





buy_starter_keybaord_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒",callback_data="buy starter"),InlineKeyboardButton(text="🚫",callback_data="imkor qilish")]
    
]) 

buy_git_keyboard_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒",callback_data="buy git asoslari"),InlineKeyboardButton(text="🚫",callback_data="imkor qilish")]
    
]) 

buy_it_keyboard_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒",callback_data="buy it qadam"),InlineKeyboardButton(text="🚫",callback_data="imkor qilish")]
    
])
    
    
    
    
buy_backend_keyboard_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒",callback_data="buy backend rus"),InlineKeyboardButton(text="🚫",callback_data="imkor qilish rus")]
    
]) 

buy_front_end_keybaord_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒",callback_data="buy front-end rus"),InlineKeyboardButton(text="🚫",callback_data="imkor qilish rus")]
    
]) 

buy_dizene_keyboard_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒",callback_data="buy dizine rus"),InlineKeyboardButton(text="🚫",callback_data="imkor qilish rus")]
    
]) 





buy_starter_keybaord_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒",callback_data="buy starter rus"),InlineKeyboardButton(text="🚫",callback_data="imkor qilish rus")]
    
]) 

buy_git_keyboard_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒",callback_data="buy git asoslari rus"),InlineKeyboardButton(text="🚫",callback_data="imkor qilish rus")]
    
]) 

buy_it_keyboard_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒",callback_data="buy it qadam rus"),InlineKeyboardButton(text="🚫",callback_data="imkor qilish rus")]
    
]) 
    
    
    
    
    
    
    
    
    

about_we_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="kompaniya haqida video",url='https://youtu.be/sGmNSsG-vrQ?si=Q_Yg3mFRQFbRZuqo'),InlineKeyboardButton(text="sayt",url='https://space.marsit.uz/')]
    
])   

about_we_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="видео о компании",url='https://youtu.be/sGmNSsG-vrQ?si=Q_Yg3mFRQFbRZuqo'),InlineKeyboardButton(text="sayt",url='https://space.marsit.uz/')]
    
])      
    
    
    
    
menu_language_keyboard_uzb = [
    [KeyboardButton(text='uzbek tili 🇺🇿'),KeyboardButton(text='rus tili 🇷🇺')]
]

menu_language_button_uzb = ReplyKeyboardMarkup(keyboard=menu_language_keyboard_uzb,resize_keyboard=True)    


menu_language_keyboard_rus = [
    [KeyboardButton(text='Узбекский язык 🇺🇿'),KeyboardButton(text='русский язык 🇷🇺')]
]

menu_language_button_rus = ReplyKeyboardMarkup(keyboard=menu_language_keyboard_rus,resize_keyboard=True)      
    
    
cart_keyboard_uzb = [
    [KeyboardButton(text='Humo'),KeyboardButton(text='Uzcard')]
]

cart_button_uzb = ReplyKeyboardMarkup(keyboard=cart_keyboard_uzb,resize_keyboard=True)

cart_keyboard_rus = [
    [KeyboardButton(text='Хумо'),KeyboardButton(text='Узкард')]
]

cart_button_rus = ReplyKeyboardMarkup(keyboard=cart_keyboard_rus,resize_keyboard=True)    


menu_korzinka_keyboard_uzb = [
    [KeyboardButton(text='barcha mahsulotni sotib olish'),KeyboardButton(text='barcha mahsulotlarni olib tashlash'),KeyboardButton(text='yana mahsulot qoshish')],
    [KeyboardButton(text='ortga ⬅️')]
]

menu_korzinka_button_uzb = ReplyKeyboardMarkup(keyboard=menu_korzinka_keyboard_uzb,resize_keyboard=True)


menu_korzinka_keyboard_rus = [
    [KeyboardButton(text='купить все товары'),KeyboardButton(text='удалить все товары'),KeyboardButton(text='добавить больше продуктов')],
    [KeyboardButton(text='назад ⬅️')]
]

menu_korzinka_button_rus = ReplyKeyboardMarkup(keyboard=menu_korzinka_keyboard_rus,resize_keyboard=True)
    
    
    
    

    
@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    await message.answer('tilni tanlang',reply_markup = start_language_button)
    
    
    
    
@dp.message(F.text == "uzb 🇺🇿")
async def start_uzb(message: types.Message, state: FSMContext):
    await state.set_state(Registration_uzb.first_name)
    await message.answer("Xush kelibsiz\nIsmingizni kiriting: ", reply_markup=ReplyKeyboardRemove())
    
    
@dp.message(Registration_uzb.first_name)
async def first_name_function_uzb(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration_uzb.last_name)
    await message.answer("Yaxshi endi familya kiriting: ")


@dp.message(Registration_uzb.last_name)
async def last_name_function_uzb(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Registration_uzb.number)
    await message.answer("Yaxshi endi nomerizni kiriting: ", reply_markup=contact_button)


@dp.message(Registration_uzb.number)
async def phone_function_uzb(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"ismingiz: {data['first_name']}\nfamilyangiz: {data['last_name']}\nnomeringiz: {data['number']}", reply_markup=types.ReplyKeyboardRemove())
    await state.clear()
    await message.answer('menu',reply_markup=big_menu_button_uzb)    
    
    
    
    
    
@dp.message(F.text == "rus 🇺🇿")
async def start_rus(message: types.Message, state: FSMContext):
    await state.set_state(Registration_rus.first_name)
    await message.answer("Добро пожаловать\nВведите ваше имя:", reply_markup=ReplyKeyboardRemove())
    
    
@dp.message(Registration_rus.first_name)
async def first_name_function_rus(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration_rus.last_name)
    await message.answer("Хорошо, теперь введите свою фамилию:")


@dp.message(Registration_rus.last_name)
async def last_name_function_rus(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Registration_rus.number)
    await message.answer("Хорошо, теперь введите номер:", reply_markup=contact_button_rus)


@dp.message(Registration_rus.number)
async def phone_function_rus(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"имя:{data['first_name']}\nфамилия: {data['last_name']}\nномер: {data['number']}", reply_markup=types.ReplyKeyboardRemove())
    await state.clear()
    await message.answer('меню',reply_markup=big_menu_button_rus)    
    
    
    
@dp.message(F.text == "kurslar 🔖")
async def menu_uzb(message: types.Message):
    await message.answer('menu',reply_markup=menu_kurs_button_uzb)      
    
    
@dp.message(F.text == "backend")
async def backend_uzb(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=9bd8930040608bba1ca410f0b9c6ce872b5ee2e3-9185386-images-thumbs&n=13",caption='backendda siz python chuqir organasiz',reply_markup=buy_backend_keyboard_uzb)         
    
@dp.message(F.text == "front-end")
async def front_end_uzb(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=cba29f3dfc730fd08618450e0abf0cd98217b6d7-3693917-images-thumbs&n=13",caption='siz saytlarni maketini yasisiz',reply_markup=buy_front_end_keybaord_uzb)                   
    
@dp.message(F.text == "dizine")
async def dizine_uzb(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=cba29f3dfc730fd08618450e0abf0cd98217b6d7-3693917-images-thumbs&n=13",caption='siz yengi dizine oylab topasiz',reply_markup=buy_dizene_keyboard_uzb)         
    
    
korzinka_uzb_list = []
korzinka_rus_list = []    

korzinka_uzb_list.clear()
korzinka_rus_list.clear() 
    

@dp.message(F.text == "starter")
async def starter_uzb(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=1a7adf7566dd438ba2096d86f6ba2874b8f3b0fa41238982-5249431-images-thumbs&n=13",caption='siz aytini nimaga kerakligini bilib olasiz',reply_markup=buy_starter_keybaord_uzb)     
    
@dp.message(F.text == "git asoslari")
async def git_asoslari_uzb(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=0cd769e61778f4916e88a7d7fb1d30ee3ad9f7f0-4743742-images-thumbs&n=13",caption='gitni organasiz',reply_markup=buy_git_keyboard_uzb)     
    
@dp.message(F.text == "It sohasiga ilk qandam")
async def it_one_qadam_uzb(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=94bb3710792945777d25902f6a68650ccab6502c-5656941-images-thumbs&n=13",caption='komputerni organasiz',reply_markup=buy_it_keyboard_uzb)         
      
    
    
@dp.callback_query(F.data == 'buy backend')
async def buy_backend_uzb(callback: types.CallbackQuery):
    korzinka_uzb_list.append('backend')
    korzinka_rus_list.append('backend')   
    await callback.answer('siz backend kursini sotib oldis') 
    
@dp.callback_query(F.data == "buy front-end")
async def buy_front_end_uzb(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('front end')
    korzinka_rus_list.append('front end') 
    await callback.answer('siz front end kursini sotib oldiz')
    
@dp.callback_query(F.data == 'buy dizine')
async def buy_dizine_uzb(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('dizene')
    korzinka_rus_list.append('dizene') 
    await callback.answer('siz dizene kursini sotib oldis')   
    




@dp.callback_query(F.data == 'buy starter')
async def buy_starter_uzb(callback: types.CallbackQuery):
    korzinka_uzb_list.append('starter')
    korzinka_rus_list.append('starter')   
    await callback.answer('siz starter kursini sotib oldis') 
    
@dp.callback_query(F.data == "buy git asoslari")
async def buy_git_uzb(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('git')
    korzinka_rus_list.append('git') 
    await callback.answer('siz git kursini sotib oldiz')
    
@dp.callback_query(F.data == 'buy it qadam')
async def buy_it_uzb(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('it birinchi qadam')
    korzinka_rus_list.append('it первый шаг') 
    await callback.answer('siz it birinchi qadam sotib oldis')   
    
@dp.callback_query(F.data == 'imkor qilish')
async def never_uzb(callback: types.CallbackQuery):  
    await callback.answer('suz tovar imkor qildiz')   
    
    
    
    
    
    
    
    
    
    
    
    
    
@dp.message(F.text == "курсы 🔖")
async def menu_rus(message: types.Message):
    await message.answer('menu',reply_markup=menu_kurs_button_rus)      
    
    
@dp.message(F.text == "баккенд")
async def backend_rus(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=9bd8930040608bba1ca410f0b9c6ce872b5ee2e3-9185386-images-thumbs&n=13",caption='на бэкэнде ты глубокий орган питона',reply_markup=buy_backend_keyboard_rus)         
    
@dp.message(F.text == "фронт энд")
async def front_end_rus(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=cba29f3dfc730fd08618450e0abf0cd98217b6d7-3693917-images-thumbs&n=13",caption='ты занимаешься дизайном сайтов',reply_markup=buy_front_end_keybaord_rus)                   
    
@dp.message(F.text == "дизайн")
async def dizine_rus(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=cba29f3dfc730fd08618450e0abf0cd98217b6d7-3693917-images-thumbs&n=13",caption='ты найдешь новое колено',reply_markup=buy_dizene_keyboard_rus)         
        
    

@dp.message(F.text == "стартер")
async def starter_rus(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=1a7adf7566dd438ba2096d86f6ba2874b8f3b0fa41238982-5249431-images-thumbs&n=13",caption='ты будешь знать, что сказать',reply_markup=buy_starter_keybaord_rus)     
    
@dp.message(F.text == "основы git")
async def git_rus(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=0cd769e61778f4916e88a7d7fb1d30ee3ad9f7f0-4743742-images-thumbs&n=13",caption='ты можешь это сделать',reply_markup=buy_git_keyboard_rus)     
    
@dp.message(F.text == "Мой первый шаг в ит")
async def it_rus(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=94bb3710792945777d25902f6a68650ccab6502c-5656941-images-thumbs&n=13",caption='ты приводишь в порядок компьютер',reply_markup=buy_it_keyboard_rus)         
      
    
    
@dp.callback_query(F.data == 'buy backend rus')
async def buy_backend_rus(callback: types.CallbackQuery):
    korzinka_uzb_list.append('backend')
    korzinka_rus_list.append('backend')   
    await callback.answer('Вы приобрели курс по серверной части') 
    
@dp.callback_query(F.data == "buy front-end rus")
async def buy_front_end_rus(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('front end')
    korzinka_rus_list.append('front end') 
    await callback.answer('вы приобрели фронтальный кур')
    
@dp.callback_query(F.data == 'buy dizine rus')
async def buy_dizine_rus(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('dizene')
    korzinka_rus_list.append('dizene') 
    await callback.answer('Вы приобрели курс дизайна')   
    




@dp.callback_query(F.data == 'buy starter rus')
async def buy_mini_fri_rus(callback: types.CallbackQuery):
    korzinka_uzb_list.append('starter')
    korzinka_rus_list.append('starter')   
    await callback.answer('вы приобрели стартовый курс') 
    
@dp.callback_query(F.data == "buy git asoslari rus")
async def buy_big_fri_rus(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('git')
    korzinka_rus_list.append('git') 
    await callback.answer('вы купили курс git')
    
@dp.callback_query(F.data == 'buy it qadam rus')
async def buy_biggest_fri_rus(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('it birinchi qadam')
    korzinka_rus_list.append('it первый шаг') 
    await callback.answer('siz it birinchi qadam sotib oldis')   
    
@dp.callback_query(F.data == 'imkor qilish rus')
async def buy_biggest_fri_rus(callback: types.CallbackQuery):  
    await callback.answer('Вы отказались от товара') 
    
    
    
    
    
    
@dp.message(F.text == 'korzinka 🛒')
async def korzinka_uzb(message: types.Message):
    if korzinka_uzb_list:   
        # await message.answer(f'korzinka {korzinka_uzb_list}',reply_markup=menu_korzinka_button_uzb)
        result = "\n".join([f"{key}" for key in korzinka_uzb_list])
        await message.answer(f'{result}',reply_markup=menu_korzinka_button_uzb)   
    else:
        await message.answer('siz hali hech narsa sotib omadis')
    
@dp.message(F.text == 'корзинка 🛒')
async def korzinka_rus(message: types.Message):
    if korzinka_rus_list:   
        # await message.answer('корзинка',str(korzinka_rus_list),reply_markup=menu_korzinka_button_uzb)
        result = "\n".join([f"{key}" for key in korzinka_rus_list])
        await message.answer(f'{result}',reply_markup=menu_korzinka_button_rus)   
    else:
        await message.answer('Вы еще ничего не купили')




@dp.message(F.text == 'barcha mahsulotni sotib olish')
async def buy_products(message: types.Message):
    await message.answer('barcha mahsuotni sotib olish',reply_markup=cart_button_uzb)
    
@dp.message(F.text == 'купить все товары')
async def buy_products_rus(message: types.Message):
    await message.answer('купить все товары',reply_markup=cart_button_rus)
    
    
@dp.message(F.text == 'barcha mahsulotlarni olib tashlash')
async def remove_products_uzbb(message: types.Message):
    korzinka_uzb_list.clear()
    korzinka_uzb_list.clear()
    await message.answer('menu',reply_markup=big_menu_button_uzb)

@dp.message(F.text == 'удалить все товары')
async def remove_products_uzbb(message: types.Message):
    korzinka_uzb_list.clear()
    korzinka_uzb_list.clear()
    await message.answer('menu',reply_markup=big_menu_button_rus)
    
humo_list = []
uzcard_list = []    
    
    
    
    
    
    
    
    
    
    
    
        
@dp.message(F.text == 'Humo')
async def humo(message: types.Message, state: FSMContext):
    await state.set_state(Cart.cart_number)
    await message.answer('cartani nomereni kiriting',reply_markup=ReplyKeyboardRemove())


@dp.message(Cart.cart_number)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit():
        await state.update_data(cart_number=text)
        await message.answer('xarid qiganinggiz uchun raxmat',reply_markup=big_menu_button_uzb)
        korzinka_rus_list.clear()
        korzinka_uzb_list.clear()
    else:
        await message.answer('siz carta raqamini kiritmadiz')
    await state.clear()
        
            
     
@dp.message(F.text == 'Uzcard')
async def uzcard(message: types.Message, state: FSMContext):
    await state.set_state(Cart.cart_number)
    await message.answer('cartani nomereni kiriting',reply_markup=ReplyKeyboardRemove())


@dp.message(Cart.cart_number)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit():
        await state.update_data(cart_number=text)
        await message.answer('xarid qiganinggiz uchun raxmat',reply_markup=big_menu_button_uzb)
        korzinka_rus_list.clear()
        korzinka_uzb_list.clear()
    else:
        await message.answer('siz carta raqamini kiritmadiz')
    await state.clear()




@dp.message(F.text == 'Хумо')
async def humo_rus(message: types.Message, state: FSMContext):
    await state.set_state(Cart_ru.cart_number)
    await message.answer('введите номер карты',reply_markup=ReplyKeyboardRemove())


@dp.message(Cart_ru.cart_number)
async def card_number_function_rus(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit():
        await state.update_data(cart_number=text)
        await message.answer('Спасибо за покупку',reply_markup=big_menu_button_rus)
        korzinka_rus_list.clear()
        korzinka_uzb_list.clear()
    else:
        await message.answer('вы не ввели номер карты')
    await state.clear()
        
            
     

@dp.message(F.text == 'Узкард')
async def uzcard_rus(message: types.Message, state: FSMContext):
    await state.set_state(Cart_ru.cart_number)
    await message.answer('введите номер карты',reply_markup=ReplyKeyboardRemove())
    
    
    
@dp.message(Cart_ru.cart_number)
async def card_number_function_rus(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit():
        
        await state.update_data(cart_number=text)
        await message.answer('Спасибо за покупку',reply_markup=big_menu_button_rus)
        korzinka_rus_list.clear()
        korzinka_uzb_list.clear()
    else:
        await message.answer('вы не ввели номер карты')
    await state.clear()


        



@dp.message(F.text == 'yana mahsulot qoshish')
async def add_new_products(message: types.Message):
    await message.answer('yana mahsulot qoshish',reply_markup=big_menu_button_uzb)

@dp.message(F.text == 'добавить больше продуктов')
async def add_new_products_rus(message: types.Message):
    await message.answer('добавить больше продуктов',reply_markup=big_menu_button_rus)    
    
    
    
    
    
@dp.message(F.text == "biz haqida 👈")
async def biz_haqida_uzb(message: types.Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=f4477b0983b3f4ff0e04ec3d96dc5ac0f388fd57-10640163-images-thumbs&n=13',caption='bu 8 yoshdan boshlab 16 yoshgacha bolgan bolalar uchun moslashgan IT kurslar',reply_markup=about_we_uzb)  
    
    
@dp.message(F.text == "О нас 👈")
async def biz_haqida_rus(message: types.Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=f4477b0983b3f4ff0e04ec3d96dc5ac0f388fd57-10640163-images-thumbs&n=13',caption='Это IT-курсы, специально разработанные для детей от 8 до 16 лет',reply_markup=about_we_rus)  
    
    
    
    
    
def answer_process(question):       
    response = openai.completions.create(
        model='gpt-3.5-turbo-instruct',
        prompt=f"Hey bro, i have question to and the question is {question}."
            f"After answering please just answer in Uzbek language",
        max_tokens=1000,
    )
    if response['choices'][0]['text']:
        answer = response['choices'][0]['text']
        answer.replace("_", "\\_")
        answer.replace("*", "\\*")
        answer.replace("[", "\\[")
        answer.replace("`", "\\`")
        answer.replace("=", "\\=")
        return answer
    else:
        return "Nima deb yozding?"
    
@dp.message(F.text == "yordam 🆘")
async def yordam_uzb(message: types.Message):
    result = await answer_process(question=message.text)

    await message.answer(text=result)
       
       
@dp.message(F.text == "помощь 🆘")
async def yordam_uzb(message: types.Message):
    result = await answer_process(question=message.text)

    await message.answer(text=result)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
@dp.message(F.text == "til 🇷🇺🔄🇺🇿")
async def til_ru_uz_uzb(message: types.Message):
    await message.answer('til',reply_markup=menu_language_button_uzb)   
    
@dp.message(F.text == "язык 🇷🇺🔄🇺🇿")
async def til_ru_uz_uzb(message: types.Message):
    await message.answer('язык',reply_markup=menu_language_button_rus)  
    
    
    
    
    
@dp.message(F.text == "uzbek tili 🇺🇿")
async def uzb_uzb(message: types.Message):
    await message.answer('uzbek menu',reply_markup=big_menu_button_uzb)   
    
@dp.message(F.text == "rus tili 🇷🇺")
async def rus_uzb(message: types.Message):
    await message.answer('rus menu',reply_markup=big_menu_button_rus)
    
    
@dp.message(F.text == "Узбекский язык 🇺🇿")
async def uzb_rus(message: types.Message):
    await message.answer('Узбекское меню',reply_markup=big_menu_button_uzb)   
    
@dp.message(F.text == "русский язык 🇷🇺")
async def rus_rus(message: types.Message):
    await message.answer('Русское меню',reply_markup=big_menu_button_rus)
    
    
    
    
@dp.message(F.text == "ortga ⬅️")
async def ortga(message: types.Message):
    await message.answer('menu',reply_markup=big_menu_button_uzb)      
    
@dp.message(F.text == "назад ⬅️")
async def ortga_rus(message: types.Message):
    await message.answer('menu',reply_markup=big_menu_button_rus)   
    
    
    
async def main():
    await dp.start_polling(bot)
    
    
    
if __name__== '__main__':
    asyncio.run(main())