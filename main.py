#------------------[1] Импорт данных-------------------

import telebot
from telebot import types
import time
bot = telebot.TeleBot('There is must be a token')


#------------------[2] Вспомогательные команды-------------------
@bot.message_handler(commands=['end'])
def exit(message):
    start(message)
    operation = message.text
    if operation == 'end' :
     bot.send_message(message.chat.id, text='Хорошо, заканчиваю работу')
     start(message)


#------------------[3] Команда для работы с графиками-------------------

@bot.message_handler(commands=['graph'])
def graph(message):
    bot.send_message(message.chat.id, text='Здравствуйте, здесь вы сможете ознакомиться с основными графиками в математике а также узнать об их свойствах.')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Функция y=x²')
    btn2 = types.KeyboardButton('Функция y=k/x')
    btn3 = types.KeyboardButton('Фукнция  y = √x')
    btn4 = types.KeyboardButton('Показательная функция')
    btn5 = types.KeyboardButton('log функция')
    btn6 = types.KeyboardButton('y=sinx')
    btn7 = types.KeyboardButton('y=cosx')
    btn8 = types.KeyboardButton('y=tgx')
    btn9 = types.KeyboardButton('y= ctgx')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9,)
    time.sleep(0.8)
    operation = bot.send_message(message.chat.id, text='Выберите интересующий вас график функции', reply_markup=markup)
    bot.register_next_step_handler(operation,graph2)
def graph2(message):
    if message.text == 'Функция y=x²':
        bot.send_photo(message.chat.id,'https://lh3.googleusercontent.com/y5sLIxkyrlwdMey79tTOFsgYKh77v-AHG7mX_fLVbZ_iRHSw81bPuwwMQzygjsjkX1f9Tx7uQX8tGnv2jG-gVjGAmy8b8DZBHlMyVYSezxQEbLRUaOcOu-tKezOwueXbLnJzDO3o')
        time.sleep(1)
        bot.send_message(message.chat.id, text='А теперь, расскажу немного об этом графике')
        bot.send_message(message.chat.id, text='Название графика: Парабола\nОсновные свойства: \n 1) Областью определения функции  является множество всех действительных чисел т.е D(y) = (-∞;+∞)\n 2) Значение функции y=0 является наименьшим, а наибольшего значения функция не имеет.\n 3)Функция является четной, так как график симметричен относительно оси Оу\n 4)Функция непериодическая \n 5)Парабола  имеет с осями координат единственную общую точку (0;0) - начало координат.\n 6)Значение аргумента x=0 является нулем функции.\n 7)На промежутке (-∞;0] функция убывающая, а на промежутке [0;+∞)  - возрастающая.')
        time.sleep(1.5)
        end=bot.send_message(message.chat.id,text='!!!ВНИМАНИЕ!!!\n Чтобы вернуться в меню выбора функций,нажмите /back\n Чтобы вернуться в начальное меню, нажмите /end')
        bot.register_next_step_handler(end, options)
    elif message.text == 'Функция y=k/x':
        bot.send_photo(message.chat.id,'https://ru-static.z-dn.net/files/db1/8f3bae49c7a9213c961846dfc129bf13.png')
        time.sleep(1)
        bot.send_message(message.chat.id, text='А теперь, расскажу немного об этом графике')
        bot.send_message(message.chat.id,text='Название графика: Гипербола\nОсновные свойства: \n 1) Область определения: все числа, кроме х=0.\n 2) Область значений:(−∞;0)U(0;+∞).\n 3)Наибольшего и наименьшего значений нет.\n 4)Функция убывает на промежутках: (−∞;0)и(0;+∞) если k>0, и возрастает на этих же промежутках при условии что k<0 . \n 5)Гипербола является нечётной функцией\n ')
        time.sleep(1.5)
        end=bot.send_message(message.chat.id, text='!!!ВНИМАНИЕ!!!\n Чтобы вернуться в меню выбора функций,нажмите /back\n Чтобы вернуться в начальное меню, нажмите /end')
        bot.register_next_step_handler(end, options)
    elif message.text == 'Фукнция  y = √x':
        bot.send_photo(message.chat.id, 'https://2012books.lardbucket.org/books/beginning-algebra/section_11/0a9231628a85c0cbd5504cc9d9ec3621.jpg')
        time.sleep(1)
        bot.send_message(message.chat.id, text='А теперь, расскажу немного об этом графике')
        bot.send_message(message.chat.id,
                         text='Название графика: Функция квадратного корня \nОсновные свойства: \n 1) Область определения:[0;+∞).\n 2)Чем больше х, тем больше у. Значит наша функция возрастает, то есть мы движемся, как будто "в горку". Функция возрастает на всей области определения.\n 3)Из графика хорошо видно, что наименьшее значение функции равно 0 при х=0. Наибольшего значения нет, так как функция постоянно растет.\n 4)Данная функиция является непрерывной. Мы не видим ни каких точек разрыва, везде проходит сплошная линия. \n 5)Так как х не может быть отрицательным, то чётность этой функции не рассматривается. Она не является ни чётной, ни нечётной\n ')
        time.sleep(1.5)
        end=bot.send_message(message.chat.id, text='!!!ВНИМАНИЕ!!!\n Чтобы вернуться в меню выбора функций,нажмите /back\n Чтобы вернуться в начальное меню, нажмите /end')
        bot.register_next_step_handler(end,options)
    elif message.text =='Показательная функция':
        bot.send_photo(message.chat.id, 'https://matica.org.ua/images/stories/26042021/image2548.png')
        time.sleep(1)
        bot.send_message(message.chat.id, text='А теперь, расскажу немного об этом графике')
        bot.send_message(message.chat.id,text='Название графика: График показательной функции\nОсновные свойства: \n 1) Область определения функции −  множество R действительных чисел\n 2) Область значений: (0;+∞).\n 3) Функция ни четная, ни нечетная\n 4) Не ограничена сверху, ограничена снизу \n 5) Не имеет ни наибольшего, ни наименьшего значений\n 6) Показательная функция не имеет точек экстремума, то есть она не имеет точек минимума и максимума функции.\n 7) График любой показательной функции проходит через точку (0;1)\n')
        time.sleep(1.5)
        end = bot.send_message(message.chat.id,
                               text='!!!ВНИМАНИЕ!!!\n Чтобы вернуться в меню выбора функций,нажмите /back\n Чтобы вернуться в начальное меню, нажмите /end')
        bot.register_next_step_handler(end, options)
    elif message.text == 'log функция':
        bot.send_photo(message.chat.id,'https://www.webmath.ru/poleznoe/images/graph_365.GIF')
        time.sleep(1)
        bot.send_message(message.chat.id, text='А теперь, расскажу немного об этом графике')
        bot.send_message(message.chat.id,
                         text='Название графика: График логарифмической функции\nОсновные свойства: \n 1) Областью определения функции является множество всех положительных чисел (0;+∞)\n 2) Область значений  - y є R \n 3) Функция ни четная, ни нечетная\n 4) Функция непериодическая. \n 5) Нули функции. График функции пересекает координатную ось Ox в точке (1;0).\n 6) Наименьшего и наибольшего значений функция не имеет\n 7) При a>1 функция возрастает; при 0<а<1 функция убывает\n')
        time.sleep(1.5)
        end = bot.send_message(message.chat.id,
                               text='!!!ВНИМАНИЕ!!!\n Чтобы вернуться в меню выбора функций,нажмите /back\n Чтобы вернуться в начальное меню, нажмите /end')
        bot.register_next_step_handler(end, options)
    elif message.text == 'y=sinx':
        bot.send_photo(message.chat.id,'https://ru-static.z-dn.net/files/d5c/cab5f16157f85cdbac37699170233e5b.png')
        time.sleep(1)
        bot.send_message(message.chat.id, text='А теперь, расскажу немного об этом графике')
        bot.send_message(message.chat.id,
                         text='Название графика: Синусоида\nОсновные свойства: \n 1) Областью определения функции является множество всех действительных чисел т.е  x є R\n 2) Область значений  - [-1;1] \n 3) Функция является нечетной\n 4) Функция периодическая. \n 5) Функция принимает положительные значения на промежутках (2пk;п+2пk), k є Z\n 6) Функция принимает отрицательные значения на промежутках (-п+2пk;2пk) k є Z\n 7) Точки минимума - (-П/2+2пk;-1), k є Z\n 8) Точки максимума - (П/2+2пk;1), k є Z\n')
        time.sleep(1.5)
        end = bot.send_message(message.chat.id,
                               text='!!!ВНИМАНИЕ!!!\n Чтобы вернуться в меню выбора функций,нажмите /back\n Чтобы вернуться в начальное меню, нажмите /end')
        bot.register_next_step_handler(end, options)
    elif message.text == 'y=cosx':
        bot.send_photo(message.chat.id,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3WcT3yTv8jM5-Bw79btASSWxUxaLf4-IYsQ&usqp=CAU')
        time.sleep(1)
        bot.send_message(message.chat.id, text='А теперь, расскажу немного об этом графике')
        bot.send_message(message.chat.id,
                         text='Название графика: Косинусоида\nОсновные свойства: \n 1) Областью определения функции является множество всех действительных чисел т.е  x є R\n 2) Область значений  - [-1;1] \n 3) Функция является четной\n 4) Функция периодическая. \n 5) Функция принимает положительные значения на промежутках (-п/2+2пk;п+2пk), k є Z\n 6) Функция принимает отрицательные значения на промежутках (п/2+2пk;3п/2+2пk) k є Z\n 7) Точки минимума - (П+2пk;-1), k є Z\n 8) Точки максимума - (2пk;1), k є Z\n')
        time.sleep(1.5)
        end = bot.send_message(message.chat.id,
                               text='!!!ВНИМАНИЕ!!!\n Чтобы вернуться в меню выбора функций,нажмите /back\n Чтобы вернуться в начальное меню, нажмите /end')
        bot.register_next_step_handler(end, options)
    elif message.text == 'y=tgx':
        bot.send_photo(message.chat.id,'https://resh.edu.ru/uploads/lesson_extract/3943/20190730111950/OEBPS/objects/c_matan_11_5_1/f2345f5c-c072-42f9-83f1-69bfb002e7fc.png')
        time.sleep(1)
        bot.send_message(message.chat.id, text='А теперь, расскажу немного об этом графике')
        bot.send_message(message.chat.id,
                         text='Название графика: Тангенсоида\nОсновные свойства: \n 1) Областью определения функции является множество всех действительных чисел кроме случая когда x = п/2 + пk, k є Z\n 2) Область значений  - y є R \n 3) Функция является нечетной\n 4) Функция периодическая. \n 5) Функция принимает положительные значения на промежутках (пk;п/2 + пk), k є Z\n 6) Функция принимает отрицательные значения на промежутках (-п/2+пk;пk) k є Z\n 7) Точки минимума - отсутствуют, k є Z\n 8) Точки максимума - отсутствуют\n')
        time.sleep(1.5)
        end = bot.send_message(message.chat.id,text='!!!ВНИМАНИЕ!!!\n Чтобы вернуться в меню выбора функций,нажмите /back\n Чтобы вернуться в начальное меню, нажмите /end')
        bot.register_next_step_handler(end, options)
    elif message.text == 'y= ctgx':
        bot.send_photo(message.chat.id,'https://ykl-res.azureedge.net/14015cf2-da99-44b4-825d-49206890c24d/ctgx.png')
        time.sleep(1)
        bot.send_message(message.chat.id, text='А теперь, расскажу немного об этом графике')
        bot.send_message(message.chat.id,
                         text='Название графика: Котангенсоида\nОсновные свойства: \n 1) Областью определения функции является множество всех действительных чисел кроме случая когда x = пk, k є Z\n 2) Область значений  - y є R \n 3) Функция является нечетной\n 4) Функция периодическая. \n 5) Функция принимает положительные значения на промежутках (пk;п/2 + пk), k є Z\n 6) Функция принимает отрицательные значения на промежутках (-п/2+пk;пk) k є Z\n 7) Точки минимума - отсутствуют, k є Z\n 8) Точки максимума - отсутствуют\n')
        time.sleep(1.5)
        end = bot.send_message(message.chat.id,
                               text='!!!ВНИМАНИЕ!!!\n Чтобы вернуться в меню выбора функций,нажмите /back\n Чтобы вернуться в начальное меню, нажмите /end')
        bot.register_next_step_handler(end, options)
    elif message.text == '/end':
        bot.send_message(message.chat.id, text='Хорошо. Останавливаю все процессы и начинаю работу наново...')
        start(message)
    else:
        bot.send_message(message.chat.id, text='Пожалуйста, не используйте ничего кроме кнопок.')
        graph(message)
def options(message):
    if message.text == '/back':
        graph(message)
    elif message.text == '/end':
        bot.send_message(message.chat.id, text='Хорошо. Останавливаю все процессы и начинаю работу наново...')
        start(message)
    else:
        notrule=bot.send_message(message.chat.id, text='Пожалуйста, не нарушайте правил')
        bot.register_next_step_handler(notrule,options)


#------------------[4] Начало работы с ботом -------------------
@bot.message_handler(commands=['start'])
def start(message) :
    time.sleep(1)
    messy=bot.send_message(message.chat.id, text=' Здравствуй,пользователь, введи /calc для начала расчёта.\n----------------------\nИли же нажми /graph , чтобы ознакомиться с некоторыми графиками функций')
    bot.register_next_step_handler(messy,check1)
def check1(message):
    operation = message.text
    if  operation == '/calc':
      calculate(message)
    elif operation == '/end':
        bot.send_message(message.chat.id, text='Хорошо. Останавливаю все процессы и начинаю работу наново...')
        exit(message)
    elif operation == '/graph':
        graph(message)
    elif operation == '/start':
        start(message)
    else:
      time.sleep(1)
      bot.send_message(message.chat.id,'Пожалуйста, не нарушайте правил пользования ботом.')
      start(message)
@bot.message_handler(commands=['calc'])
def calculate(message) :
    time.sleep(0.5)
    numberone = bot.send_message(message.chat.id, "Введите первое число")
    bot.register_next_step_handler(numberone,check11)



#------------------[5] Проверка на наличие int первого числа-------------------
def check11(message):
    if message.text== '/end':
        bot.send_message(message.chat.id,text='Хорошо. Останавливаю все процессы и начинаю работу наново...')
        start(message)
    else:
        check2(message)
def check2(message):
    try:
      int(message.text)
      bot.send_message(message.chat.id,text='Цифра сохранена')
      numnum(message)
    except ValueError:
     bot.send_message(message.chat.id,  text='Похоже вы отправили фотографию или же текст. Пожалуйста, не нарушайте правила, и вписывайте исключительно числа')
     calculate(message)
    except TypeError:
        bot.send_message(message.chat.id, text='Похоже вы отправили фотографию или же текст. Пожалуйста, не нарушайте правила, и вписывайте исключительно числа')
        calculate(message)



#------------------[6] Проверка на наличие int второго числа-------------------
def numnum(message):
    global num1
    num1 = message.text
    time.sleep(0.5)
    numbertwo = bot.send_message(message.chat.id, "Введите второе число")
    bot.register_next_step_handler(numbertwo, check22)
def check22(message):
    if message.text== '/end':
        bot.send_message(message.chat.id,text='Хорошо. Останавливаю все процессы и начинаю работу наново...')
        start(message)
    else:
        check3(message)
def check3(message):
    try:
     int(message.text)
     bot.send_message(message.chat.id,text='Цифра сохранена')
     butbut(message)
    except ValueError :
     bot.send_message(message.chat.id,  text='Похоже вы отправили фотографию или же текст. Пожалуйста, не нарушайте правила, и вписывайте исключительно числа')
     calculate(message)
    except TypeError:
     bot.send_message(message.chat.id, text='Похоже вы отправили фотографию или же текст. Пожалуйста, не нарушайте правила, и вписывайте исключительно числа')
     calculate(message)


#------------------[7] Кнопки-------------------
def butbut(message):
    global num2
    num2 = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Умножение')
    btn2 = types.KeyboardButton('Деление')
    btn3 = types.KeyboardButton('Сложение')
    btn4 = types.KeyboardButton('Вычитание')
    markup.add(btn1, btn2, btn3, btn4)
    operation = bot.send_message(message.chat.id, text='Выбери нужное тебе действие', reply_markup=markup)
    bot.register_next_step_handler(operation, check33)
def check33(message):
    if message.text == '/end':
        bot.send_message(message.chat.id, text='Хорошо. Останавливаю все процессы и начинаю работу наново...')
        start(message)
    else:
        bot.send_message(message.chat.id, text='Веду расчёт....')
        result(message)

#------------------[8] Результат-------------------

def result(message):
    global operation
    operation = str(message.text)
    try:
     if operation == 'Умножение':
        resylt = int(num1) * int(num2)
        time.sleep(1)
        bot.send_message(message.chat.id, text='Вот ваш результат:☛'' ' + str(resylt))
        bot.send_message(message.chat.id, text='Чтобы вновь воспользоваться услугами бота, нажмите /end')
     elif operation == 'Деление':
        resylt = int(num1) / int(num2)
        time.sleep(1)
        bot.send_message(message.chat.id,text='Вот ваш результат:☛'' '+str(resylt))
        bot.send_message(message.chat.id, text='Чтобы вновь воспользоваться услугами бота, нажмите /end')
     elif operation == 'Сложение' :
        resylt = int(num1) + int(num2)
        time.sleep(1)
        bot.send_message(message.chat.id, text='Вот ваш результат:☛'' ' + str(resylt))
        bot.send_message(message.chat.id, text='Чтобы вновь воспользоваться услугами бота, нажмите /end')
     elif operation == 'Вычитание' :
        resylt = int(num1) - int(num2)
        time.sleep(1)
        bot.send_message(message.chat.id, text='Вот ваш результат:☛'' ' + str(resylt))
        bot.send_message(message.chat.id, text='Чтобы вновь воспользоваться услугами бота, нажмите /end')
     else:
        time.sleep(1)
        bot.send_message(message.chat.id,text='Бот не сможет обработать ваш запрос, так как вы вввели текст или отправили файл/голосовое сообщение, которое не предусмотрено ботом. Пожалуйста не нарушайте правил и следуйте указанием бота. ')
        calculate(message)
    except ValueError:
        time.sleep(1)
        bot.send_message(message.chat.id,text='Возникла ошибка, судя по всему бот не смог обработать ваш запрос.')
        calculate(message)
    except TypeError:
        time.sleep(1)
        bot.send_message(message.chat.id, text='Возникла ошибка, судя по всему бот не смог обработать ваш запрос.')
        calculate(message)
    except ZeroDivisionError:
            bot.send_message(message.chat.id, text='На ноль делить...НЕЛЬЗЯ')
            calculate(message)
bot.polling(non_stop=True)
