
to_do = []
 
while True:
    print("1.Додати завдання 2.Видалити завдання \n 3.Позначення завдання як виконане 4.видаляння завдання 5.нажміть 'q' щоб вийти")
    player_input = input(':')

    if player_input == '1':
        new_task = input('введіть нове завдання:')
        add = [new_task, 'невиконане']
        to_do.append(add)
        print(to_do)