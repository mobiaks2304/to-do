
to_do = []
 
while True:
    print("1.Додати завдання 2.Видалити завдання 3.перегляд завдань \n 4.Позначення завдання як виконане 5.нажміть 'q' щоб вийти")
    player_input = input(':')

    if player_input == '1':
        new_task = input('введіть нове завдання:')
        
        to_do.append(new_task)
        
    if player_input == '2':
        delete = input('введіть номер завдання яке хочете видалити:')
        to_do.remove(delete - 1)
    
    if player_input == '3':
        print(to_do)

