to_do = []

while True:
    print("1.Додати завдання 2.Видалити завдання \n 3.Позначення завдання як виконане 4.видалити  завдання 5.нажміть 'q' щоб вийти")
    player_input = input(':')

    if player_input == '1':
        add = input('введіть завдання:')
        to_do.append(add)
    
    if player_input == '2':
        remove = int(input('введіть номер завдання яке хочете видалити:'))
        to_do.remove(remove - 1)
        
    
    

    
