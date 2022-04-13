import view
def find_contact():
    s=True
    while s:
        find = input('Введите имя или фамилию для поиска: ').lower()
        with open('FIO.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if find in line.lower():
                    print(f'Контакт найден: {line}') 
                    s=False
                    view.hello_user()
                else:
                    print('Такого контакта не существует')
