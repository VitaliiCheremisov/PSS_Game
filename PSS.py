a = 0
b = 0
import random

while True:
    start = input("Введите stone, paper, scissors для начала игры, score для таблицы, Win score для самой "
                  "большой серии побед, exit для выхода из игры: ")
    moves = ['stone', 'paper', 'scissors']
    comp = random.choice(moves)


    def convert(comp):
        if comp == 'scissors':
            c = ('''  :**.    .**: 
            *+.::*  **: **
            :*: *+..++ :**
             -+*++***+*+- 
                .=*%=.    
                 -%+*     
                :**+:+    
               :*::.*:+   
              .+:*  .*:*  
              .+*    .**  
               *      -- ''')
            return c
        if comp == 'stone':
            c = ('''     -=%#%@%+**:.    
               :@#@%@%%@@@@@:   
              *%@@=%%@@=+=%%@+  
              =%##=%@@%+++==@*  
            ...+%@@@####@@#%:.. 
              .-+#@#######%*..  ''')
            return c
        if comp == 'paper':
            c = ('''             ..-...-
                    .  -.....---
                ..-.......----- 
             .........-----:    
             ---....-----       
            .-*:-----           
              ----              ''')
            return c


    if start == 'exit':
        print('Game over')
        break
    if start == 'score':
        print(f'Комп Игрок')
        print(f'{b}    {a}')
    if start == 'Win strike':
        if a > b:
            print(f'Cерия побед Игрока {a}')
        elif a < b:
            print(f'Серия побед Компа {b}')
        else:
            print(f'У Вас и компа одинаковое число побед {a} и {b}')
    if start == 'stone' or start == 'paper' or start == 'scissors':
        print(f'Ход Игрока {start}')
        print(f'Ход Компа {convert(comp)}')
        if start == comp:
            print(f'Игрок и Комп выбрали одинаковый ход. Ничья!')
        elif start == 'stone':
            if comp == 'paper':
                b = b + 1
                print(f'Игрок проиграл!')
            else:
                a = a + 1
                print(f'Игрок выиграл!')
        elif start == 'scissors':
            if comp == 'stone':
                b = b + 1
                print(f'Игрок проиграл!')
            else:
                a = a + 1
                print(f'Игрок выиграл!')
        elif start == 'paper':
            if comp == 'scissors':
                b = b + 1
                print(f'Игрок проиграл!')
            else:
                a = a + 1
                print(f'Игрок выиграл!')
    elif start != 'exit' or start != 'Win strike' or start != 'paper' or start != 'stone' or start != 'scissors' or start != 'score':
        print('Неверный ввод, повторите команду')
