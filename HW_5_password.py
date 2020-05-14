"""
Создать переменную password и сохранить в неё любую комбинацию символов.
У пользователя запросить пароль. Проверить пароль на совпадение с password и выводить соответствующее сообщение.
Дополнительно: разрешать только три попытки на ввод пароля.
"""
# todo добавить проверку имени пользователя
user_name = ''
password = 'Jkj*^83J3'
attempts = 0
while attempts < 3:
    check = input('Введите пароль:')
    if password == check:
        print('Пароль верный')
        exit()
    attempts += 1
    message = 'Пароль введен не верно'
    # message = message + '. Вы заблокированы' if attempts == 3 else message + ', повторите'
    message += '. Вы заблокированы' if attempts == 3 else ', повторите'
    print(message)

