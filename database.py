import sqlite3

global db, sql

db = sqlite3.connect('аккаунты.db')
sql = db.cursor()
conn = sqlite3.connect('аккаунты.db', check_same_thread=False)

sql.execute("""CREATE TABLE IF NOT EXISTS users (login TEXT,
    user_class TEXT,
    user_id BIGINT
)""")


def reg():
    db.commit()
    user_login = input('Login: ')
    user_class = input('Class: ')
    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?,?,?)", (user_login, user_class, 0))
        db.commit()
        print('Зарегистрировано')
    else:
        print("Такая запись уже имеется!")
        mess = 'Такая запись уже имеется'
        for value in sql.execute("SELECT * FROM users"):
            print(value[0])
            # mess = mess + '\n' + value


def login():
    user_login = input("Войти: ")
    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    if sql.fetchone() is None:
        print('Такого логина не существует. Зарегистрируйтесь')
        reg()
    else:
        sql.execute(f'UPDATE users SET user_id = {5048652373} WHERE login = "{user_login}"')
        db.commit()
        print('Привет '+user_login)


def vnutri():
    # for i in sql.execute('SELECT login, class FROM users'):
    #     print (i)
    #     # mess = mess + '\n' + i
    pass


def main():
    login()
    vnutri()


main()
