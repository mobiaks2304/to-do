import csv
to_do = []
status = []
while True:
    print("1.Додати завдання 2.Видалити завдання 3.перегляд завдань \n 4.Позначення завдання як виконане 5.нажміть 'q' щоб вийти")
    player_input = input(':')

    if player_input == '1':
        new_task = input('введіть нове завдання:')
        status.append('невиконане')
        to_do.append(new_task)
        print(to_do,status)
    if player_input == '2':
        delete = input('введіть номер завдання яке хочете видалити:')
        to_do.remove(delete - 1)
    
    if player_input == '3':
        print(to_do)

    if player_input == '4':
        stat = int(input('введіть номер завдання статус якого хочете поміняти:'))
        status[stat - 1] = 'виконане'
        
    with open('todo.csv','w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(to_do)
        writer.writerow(status)

        


