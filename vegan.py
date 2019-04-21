import os
import telebot
import emoji
from emoji import emojize
from telebot import types
#bot = telebot.TeleBot(os.environ['token'])
bot = telebot.TeleBot('899322145:AAFJHERvFRuCpEsagPeSWpJeDC036-UKDrA')
#variables
e = emoji.emojize
boom = e(':boom:', use_aliases = True)
energy = e(':zap:', use_aliases = True)
accur = e(':dart:', use_aliases = True)
fist = e(':fist:', use_aliases = True)
uron = "Урон: "
energia = "Энергия/Выстрел: "
accuracy = "Точность выстрела(%, 5-1 энергии): "
accuraci = "Точность попадания(%, 8-1 энергии): "
accuracy_with_aim = "Точность выстрела с прицелом: "
line = '*______________________________________*'
spec = "Особенность: "
group_list = '@mtsgameh\n@LastVegan'

#/help, /start
@bot.message_handler(commands=['help','start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Привет! Я помогу тебе с поиском информации по игре [VeganWars](t.me/veganwarsbot)!\nСписок команд:\n/weapons - Оружие\n/perks - Способности(перки)\n/items - Предметы\n**\nБот находтся на стадии разработки!!', parse_mode = 'markdown')

#/grouplist
@bot.message_handler(commands=['grouplist'])
def send_group_list(message):
    bot.send_message(message.chat.id, "Некоторые из групп, в которых можно поиграть в [VeganWars](t.me/veganwarsbot)\n" + group_list, parse_mode = 'markdown', disable_web_page_preview = True)

#/feedback
@bot.message_handler(commands=['feedback'])
def feedback_work(message):
    if message.text in ['/feedback', '/feedback ']:
        bot.send_message(message.chat.id, "Напишите предложение или отзыв после /feedback, в том же сообщения, что и команда")
    else:
        bot.forward_message(500238135, message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Спасибо за ваше предложение/отзыв, ваше мнение очень важно нам")

#temp
@bot.message_handler(commands=['perks', 'items'])
def send_error(message):
    bot.send_message(message.chat.id, 'Извините, функция недоступна, т.к. бот находится на стадии разработки')


#WEAPONS__________________________________________________________________________________________________________________________________________________!
#_________________________________________________________________________________________________________________________________________________________!

#Keyboard_lvl_1
@bot.message_handler(commands=['weapons'])
def send_weapons(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    distant_b = types.KeyboardButton('Оружие дальнего боя')
    close_b = types.KeyboardButton('Оружие ближнего боя')
    super_b = types.KeyboardButton('Наградное оружие')
    _exit_ = types.KeyboardButton("Выход")
    markup.add(distant_b, close_b, super_b, _exit_)
    msg = bot.send_message(message.chat.id, 'Выберите тип оружия:', reply_markup=markup)
    bot.register_next_step_handler(message, send_distant_weapons)


#Keyboard_lvl_2
def send_distant_weapons(message):
    list = ['Оружие дальнего боя', 'Дробовик', "Револьвер", "Огнемет", "Снайперская винтовка", "Пистолет", "Обрез"]
    list2 = ['Оружие ближнего боя', 'Цепь', 'Факел', 'Копье', 'Топор', 'Нож', 'Полицейская дубинка', 'Бейсбольная бита', 'Кастет', 'Кувалда', 'Булава']
    list3 = ['Наградное оружие', 'Лук Асгард', 'Катана', 'Копье Нарсил']
    if message.text in list:
        markup_distant = types.ReplyKeyboardMarkup(row_width=1)
        kb = types.KeyboardButton
        revolver = kb("Револьвер")
        firegun = kb("Огнемет")
        shotgun = kb("Дробовик")
        sniper = kb("Снайперская винтовка")
        pistol = kb("Пистолет")
        shotgunn = kb("Обрез")
        _exit_ = kb("Выход")
        back = kb("Назад")
        markup_distant.add(revolver, firegun, shotgun, sniper, pistol, shotgunn, back, _exit_)
        msg = bot.send_message(message.chat.id, 'Выберите оружие:', reply_markup=markup_distant)
        bot.register_next_step_handler(message, send_weapon_info)
    elif message.text in list2:
        markup_close = types.ReplyKeyboardMarkup(row_width=2)
        k = types.KeyboardButton
        itm0 = k(list2[1])
        itm1 = k(list2[2])
        itm2 = k(list2[3])
        itm3 = k(list2[4])
        itm4 = k(list2[5])
        itm5 = k(list2[6])
        itm6 = k(list2[7])
        itm7 = k(list2[8])
        itm8 = k(list2[9])
        itm9 = k(list2[10])
        __exit__ = k('Выход')
        back = k("Назад")        
        markup_close.add(itm0, itm1,itm2,itm3,itm4,itm5,itm6,itm7,itm8, itm9, back, __exit__)
        bot.send_message(message.chat.id, 'Выберите оружие:', reply_markup = markup_close)
        bot.register_next_step_handler(message, send_arm_info)
    elif message.text in list3:
        markup_super = types.ReplyKeyboardMarkup(row_width=1)
        k = types.KeyboardButton
        s0 = k(list3[1])
        s1 = k(list3[2])
        s2 = k(list3[3])
        __exit__ = k("Выход")
        back = k("Назад")
        markup_super.add(s0, s1, s2, back, __exit__)
        bot.send_message(message.chat.id, "Выберите оружие:", reply_markup = markup_super)
        bot.register_next_step_handler(message, send_superweapon_info)
    elif message.text == 'Выход':
        markup_rem = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Quit. /help', reply_markup = markup_rem)
    elif message.text not in list and message.text not in list2 and message.text not in list3:
        send_weapons(message)
        
#Nagradnoye oruzhue        
def send_superweapon_info(message):
    list = ['Наградное оружие', 'Лук Асгард', 'Катана', 'Копье Нарсил', "/help", "/weapons", "/start", "/perks", "/items", "Назад", "/main"]
    if message.text == 'Выход':
        markup_rem = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Quit. /help', reply_markup = markup_rem)
    elif message.text == 'Лук Асгард':
        bot.send_message(message.chat.id, "ЗАСЕКРЕЧЕНО! Наши разведчики собирают информацию...")
        send_distant_weapons(message)
    elif message.text == 'Катана':
        bot.send_message(message.chat.id, "ЗАСЕКРЕЧЕНО! Наши разведчики собирают информацию...")
        send_distant_weapons(message)
    elif message.text == 'Копье Нарсил':
        bot.send_message(message.chat.id, "Обычное копье с несколькими отличиями:\n1)Контратака стоит 3 энергии вместо 2\n2)Копье можно метнуть (затем нужно его поднять для дальнейшего использования) . Стоит 3 энергии, наносит 2-6 урона.")
        send_distant_weapons(message)
    elif message.text == 'Назад':
        send_weapons(message)
    elif message.text not in list:
        send_distant_weapons(message)
        
#Oruzhie dalnego boya        
def send_weapon_info(message):
    list = ['Оружие дальнего боя', 'Дробовик', "Револьвер", "Огнемет", "Снайперская винтовка", "Пистолет", "Обрез", "/help", "/weapons", "/start", "/perks", "/items", "Назад", "/main"]
    if message.text == 'Выход':
        markup_rem = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Quit. /help', reply_markup = markup_rem)
    elif message.text == 'Револьвер':
        bot.send_message(message.chat.id, "_РЕВОЛЬВЕР_\n" + line + "\n\n" + boom + uron + "`3`\n" + energy + energia + "`3`\n" + accur + accuracy + "`80-70-60-50-40`\n" + accur + accuracy_with_aim + "`100-90-80-60`\n" + spec + "_None_", parse_mode = 'markdown')
        send_distant_weapons(message)
    elif message.text == 'Огнемет':
        bot.send_message(message.chat.id, "_ОГНЕМЕТ_\n" + line + "\n\n" + boom + uron + "`1`\n" + energy + energia + "`3`\n" + accur + accuracy + "`80-?-60-50-40`\n" + accur + accuracy_with_aim + "_TODO_\n" + spec + "_Поджигает цель_", parse_mode = 'markdown')
        send_distant_weapons(message)
    elif message.text == 'Дробовик':
        bot.send_message(message.chat.id, "_ДРОБОВИК_\n" + line + "\n\n" + boom + uron + "`2-7`\n" + energy + energia + "`4`\n" + accur + accuracy + "`88-73-46-0-0`\n" + accur + accuracy_with_aim + "`99-88-72-64-46`\n" + spec + "_+1 урона, если стрелять в игрока, который стоит вплотную_", parse_mode = 'markdown')
        send_distant_weapons(message) 
    elif message.text == 'Снайперская винтовка':
        bot.send_message(message.chat.id, "_СНАЙПЕРСКАЯ ВИНТОВКА_\n" + line + "\n\n" + boom + uron + "`8`\n" + energy + energia + "`5`\n" + accur + accuracy + "`10-?-?-?-?`\n" + accur + accuracy_with_aim + "`40-?-20-?-?`\n" + spec + "_точность можно повышать, выцеливая игрока. При выцеливании другого, точность сбрасывается_", parse_mode = 'markdown')
        send_distant_weapons(message)
    elif message.text == 'Пистолет':
        bot.send_message(message.chat.id, "_ПИСТОЛЕТ_\n" + line + "\n\n" + boom + uron + "`2-3`\n" + energy + energia + "`3`\n" + accur + accuracy + "`91-?-75-64-51`\n" + accur + accuracy_with_aim + "`99-?-91-?-84-?`\n" + spec + "_None_", parse_mode = 'markdown')
        send_distant_weapons(message)
    elif message.text == 'Обрез':
        bot.send_message(message.chat.id, "_ОБРЕЗ_\n" + line + "\n\n" + boom + uron + "`1-4`\n" + energy + energia + "`3`\n" + accur + accuracy + "`97-?-87-75-59`\n" + accur + accuracy_with_aim + "`?`\n" + spec + "_None_", parse_mode = 'markdown')
        send_distant_weapons(message)
    elif message.text == 'Назад':
        send_weapons(message)
    elif message.text not in list:
        send_distant_weapons(message)

#Oruzhie blizhnego boya
def send_arm_info(message):
    list = ['Оружие ближнего боя', 'Цепь', 'Факел', 'Копье', 'Топор', 'Нож', 'Полицейская дубинка', 'Бейсбольная бита', 'Кастет', 'Кувалда', 'Булава',"/help", "/weapons", "/start", "/perks", "/items", "Назад", "/main"]
    ur = line + "\n\n" + fist+uron
    en = energy+energia
    ac = accur+accuraci+"`100-99-99-97-93-87-78-65`\n"
    if message.text == 'Выход':
        markup_rem = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Quit. /help', reply_markup = markup_rem)
    elif message.text == 'Цепь':
        bot.send_message(message.chat.id, "_ЦЕПЬ_\n" + ur + "`1-3`\n" + en + "`2`\n" + ac + spec + "_позволяет каждую вторую атаку выбить оружие из рук противника и нанести 2 урона_", parse_mode = 'markdown')
        send_distant_weapons(message)
    elif message.text == 'Факел':
        bot.send_message(message.chat.id, "_ФАКЕЛ_\n" + ur + "`1-3`\n" + en + "`2`\n" + ac + spec + "_c вероятностью 50% поджигает_", parse_mode = 'markdown')
        send_distant_weapons(message)
    elif message.text == 'Копье':
        bot.send_message(message.chat.id, "_Копье_\n" + ur + "`1-4`\n" + en + "`3`\n" + ac + spec + '_позволяет каждую вторую атаку использовать специальный прием "Контратака": бьет всех соперников (не более двух), которые использовали оружие в этот ход. Тратит 2 энергии._', parse_mode = 'markdown')
        send_distant_weapons(message)
    elif message.text == 'Топор':
        bot.send_message(message.chat.id, "_ТОПОР_\n" + ur + "`1-3`\n" + en + "`2`\n" + ac + spec + '_c вероятностью в 70% калечит соперника_', parse_mode = 'markdown')
        send_distant_weapons(message)
    elif message.text == 'Нож':
        bot.send_message(message.chat.id, "_НОЖ_\n" + ur + "`1-2`\n" + en + "`2`\n" + ac + spec + '_c вероятностью в 50% вызывает кровотечение_', parse_mode = 'markdown')
        send_distant_weapons(message)
    elif message.text == 'Полицейская дубинка':
        bot.send_message(message.chat.id, "_ПОЛИЦЕСЙКАЯЯ ДУБИНКА_" + ur + "`1-3`\n" + ac + spec + '_отнимает 1 энергию у цели_', parse_mode = 'markdown')
        send_distant_weapons(message)
    elif message.text == 'Бейсбольная бита':
        bot.send_message(message.chat.id, "_БЕЙСБОЛЬНАЯ БИТА_" + ur + "`1-3`\n" + ac + spec + '_с вероятностью в 20% оглушает соперника на 1 ход_', parse_mode = 'markdown')
        send_distant_weapons(message)
    elif message.text == 'Кастет':
        bot.send_message(message.chat.id, "_КАСТЕТ_" + ur + "`1-2`\n" + ac + spec + '_отнимает 4 энергии у цели, если в момент удара цель отдыхала/перезаряжалась_', parse_mode = 'markdown')
        send_distant_weapons(message)
    elif message.text == 'Булава':
        bot.send_message(message.chat.id, "БУЛАВА" + line + "\n\n" + "Информация собирается, если у вас есть, что сказать по поводу булавы, пишите /feedback", parse_mode = 'markdown')
        send_distant_weapons(message)
    elif message.text == 'Кувалда':
        bot.send_message(message.chat.id, "КУВАЛДА" + line + "\n\n" + "Информация собирается, если у вас есть, что сказать по поводу булавы, пишите /feedback", parse_mode = 'markdown')
        send_distant_weapons(message)
    elif message.text == 'Назад':
        send_weapons(message)
    elif message.text not in list:
        send_distant_weapons(message)

#MAIN_INFO________________________________________________________________________________________________________________________________________________!
#_________________________________________________________________________________________________________________________________________________________!

@bot.message_handler(commands = ['main'])
def send_main(message):
    markup_main = types.ReplyKeyboardMarkup(row_width=1)
    carac = types.KeyboardButton('Характеристики')
    do = types.KeyboardButton('Ход')
    how_to_do = types.KeyboardButton('Последовательность действий')
    _exit_ = types.KeyboardButton('Выход')
    markup_main.add(carac, do, how_to_do, _exit_)
    bot.send_message(message.chat.id, 'Выберите:', reply_markup = markup_main)
    bot.register_next_step_handler(message, send_keyboard)
    

def send_keyboard(message):
    list = ['Характеристики',"Жизнь","Энергия","Урон"]
    if message.text == 'Ход':
        send_move(message)
    elif message.text == 'Последовательность действий':
        send_order(message)
    elif message.text == 'Выход':
        markup_rem = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Quit. /help', reply_markup = markup_rem)
    elif message.text in list:
        markup_carac = types.ReplyKeyboardMarkup(row_width = 1)
        kb_life = types.KeyboardButton('Жизнь')
        kb_energy = types.KeyboardButton('Энергия')
        kb_uron = types.KeyboardButton('Урон')
        back = types.KeyboardButton("Назад")
        _exit_ = types.KeyboardButton('Выход')
        markup_carac.add(kb_life, kb_energy, kb_uron, back, _exit_)
        bot.send_message(message.chat.id, 'Выберите характеристику:', reply_markup = markup_carac)
        bot.register_next_step_handler(message, send_carac)

def send_carac(message):
    list = ["Жизнь","Энергия","Урон","Назад","Выход","/help", "/weapons", "/start", "/perks", "/items"]
    if message.text == 'Жизнь':
        bot.send_message(message.chat.id, 'Основной параметр, при потере последней жизни вы теряете сознание и не можете продолжать бой (Исключение - Зомби). Можно увеличить стартовое количество жизней с помощью Двужильности, а также восстановить 2 жизни при помощи Стимулятора.')
        send_keyboard(message)
    elif message.text == 'Энергия':
        bot.send_message(message.chat.id, 'От количества энергии зависит точность вашего оружия, а также возможность применения предметов Граната и Коктейль. Расходуется при применении вышеозначенных предметов, а также при использовании оружия.')
        send_keyboard(message)
    elif message.text == 'Урон':
        bot.send_message(message.chat.id, 'Команда, нанесшая больше урона за ход, наносит повреждения, другая не наносит повреждений.\n1-5 урона - отнимает 1 хп\n6-11 урона - отнимает 2 хп\n12-17 урона - отнимает 3 урона, и т.д.')
        send_keyboard(message)
    elif message.text == 'Назад':
        send_main(message)
    elif message.text == 'Выход':
        markup_rem = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Quit. /help', reply_markup = markup_rem)
    elif message.text == 'Ход':
        send_move(message)
    elif message.text not in list:
        send_keyboard(message)

def send_move(message):
    bot.send_message(message.chat.id, "ХОД" + line + '\n\n' + 'Есть 5 вариантов хода:\n\n*Удар/Выстрел:*\nВы используете свое оружие по назначению! (Нельзя ударить,если соперник не стоит вплотную к вам.)\n\n*Подойти (только для игроков с оружием ближнего боя):*\nВы подходите вплотную ко всем соперникам, после чего вам становится доступен удар оружием ближнего боя(Если у вас оружие ближнего боя, офк).\n\n*Отдышаться:*\nВы восстанавливаете энергию до максимума.\n\n*Пропустить/Потушиться:*\nПропускаете ход. Если вы горите - огонь тушится.\n\n*Предмет:*\nВы используете предмет из числа тех, что лежат в вашем инвентаре.', parse_mode = 'markdown')
    send_main(message)

def send_order(message):
    bot.send_message(message.chat.id, 'ПОСЛЕДОВАТЕЛЬНОСТЬ ДЕЙСТВИЙ' + line + '\n\n' '1.Применяются предметы\n\n2.Проводятся выстрелы/удары\n\n3.Те, кто выбрал вариант хода "Подойти", подходят вплотную.\n\n4.Восстанавливается энергия у игроков, выбравших вариант "Отдышаться"\n\n5.Подсчитывается урон, нанесенный обеими командами (включая горение). Все игроки команды, нанесшей меньшее количество урона, теряют X/(6-Y) [X/(10-Y), если взят Крепкий череп](целочисленное деление) +1 жизней, где Х - урон, полученный конкретным игроком (если Х = 0, игрок не теряет жизни).\n\n6.Активируются способности Пироман, Садист, Зомби, Оружейник.(если условие активации выполнено).',parse_mode = 'markdown')
    send_main(message)

bot.polling()
