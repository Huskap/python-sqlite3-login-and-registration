import sqlite3 as sql
from pprint import pprint
from time import sleep
from timeit import repeat

alphabet = {"а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о",
            "п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"} # error_catcher

con = sql.connect("accounts.db") # переменная для подключения и обращения к БД
cur = con.cursor() # переменная для манипуляций с таблицами БД


while True: # инициализация сценария входа или регистрации
    print("Зарегистрируйтесь или войдите")
    sleep(0.5)
    print("Для рестрации введите Y")
    print("Для входа введите N")
    check = input("Поле для ввода значения: ")
    sleep(1)
    if check == "N" or check == "n": # Цикл входа в аккаунт
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        statement = f"SELECT login from users WHERE login='{login}' AND Password = '{password}';" # Проверка записей по БД
        cur.execute(statement)
        if not cur.fetchone(): # error_catcher
            print("Ошибка авторизации. Логин/пароль не верны")
        else: # Успешный логин
            sleep(1)
            print("Loged IN as ADMIN")
            sleep(2)
            print("Желаете посмотерть зарегистрированные учетные записи?")
            sleep(0.5)
            print("Для просмотра введите Y")
            print("Для отмены введите N")
            see_accs = input("Поле для ввода значения: ")
            if see_accs == "N" or see_accs == "n": # Цикл на просмотр записей в БД
                print("Извините, но пока мне нечего предложить взамен :(")
                sleep(3)
                break
            elif see_accs == "Y" or see_accs == "y":
                print("Registred ACCOUNTS list...")
                sleep(1)
                state = f"SELECT login from users;"
                cur.execute(state)
                accounts = cur.fetchall()
                pprint(accounts)
                sleep(3)
                break
            else: # error_catcher
                print("Я вас не понимаю, попробуйте ввести ключ снова")
                sleep(2)
    elif check == "Y" or check == "y": # цикл создания нового пользователя
        print("Процесс регистрации нового аакаунта:")
        while True: # создание логина
            new_login = input("Введите имя пользователя: ")
            check_login = bool(alphabet.intersection(set(new_login)))
            if check_login == True: # error_catcher
                print("Пожалуйста, используйте латинскую раскладку клавиатуры!")
            else:
                break
        while True: # создание пароля
            new_password = input("Введите желаемый пароль: ")
            check_password = bool(alphabet.intersection(set(new_password)))
            if check_password == True: # error_catcher
                print("Пожалуйста, используйте латинскую раскладку клавиатуры!")
            else:
                break
        cur.execute(f"INSERT INTO users (login, password) VALUES ('{new_login}', '{new_password}');") # добавление новой записи в БД
        con.commit() # сохранение изменений в БД
    else: # error_catcher
        print("Я вас не понимаю, попробуйте ввести ключ снова")
        sleep(2)