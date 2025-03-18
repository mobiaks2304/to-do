to_do = []

while True:
    print("1.Додати завдання 2.Видалити завдання 3.перегляд завдань \n 4.Позначення завдання як виконане  5.нажміть 'q' щоб вийти")
    player_input = input(':')

    if player_input == '1':
        add = input('введіть завдання:')
        to_do.append(add)
    
    if player_input == '2':
        try:    
            remove = int(input('введіть номер завдання яке хочете видалити:'))
            to_do.remove(remove - 1)
        except ValueError:
            print('введи правильне значення')
    
    if player_input == '3':
        print(to_do)
        

