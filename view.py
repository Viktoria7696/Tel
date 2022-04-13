import read_file as rf
import add_contact as ac
import del_contact as dc
import find_contact as fc
def hello_user(): 
    print("Добро пожаловать в телефонную книгу.")
    print("""Выберете команду: 
    * list - чтобы посмотреть список контактов.
    * find - найти контакт по имени
    * add  - добавить контакт
    * del  - удаление контакта
    * edit - изменение контакта 
    * exit - выход""")
    choice=input('Введите команду: ')
    # return choice
    # while True:
    #print("\nВведите команду: ")
        # choice = input('> ')
    if choice == 'list':
        rf.read_file()
    elif choice == 'find':
        fc.find_contact()
    elif choice == 'add':
        ac.write_contact()
    elif choice == 'del':
         dc.delete()
    # elif choice == 'edit': 
    #     edit(contacts)       
    # # elif choice == 'exit':            
    else:
        print("Неизвестная команда")

    