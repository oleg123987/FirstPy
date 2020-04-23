# запросить у пользователя возраст. В зависимости от значения выводить сообщение "child", "teenager", "adult"
def check_age(age):
    if age < 14:
        print('child')
    elif 14 <= age <= 27:
        print('teenager')
    else:
        print('adult')


a = int(input('Введите возраст: '))
check_age(a)

check_age(int(input('Введите возраст: ')))

