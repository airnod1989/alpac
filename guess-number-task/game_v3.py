import numpy as np

"""Игра угадай число.
Компьютер сам загадывает и угадывает число
менее чем за 20 попыток"""


def min_score(predict_number)->int:
    
    minn=1 
    maxn=101   # задаем диапазон поиска
    count=0
    
    while True:
        count+=1
        mid=round((minn+maxn)/2) # вычесляем середину диапазона
        
        if mid > predict_number:  # с каждым циклом сужаем диапазон поиска
            maxn=mid
        elif mid < predict_number:
            minn=mid
        else:
            break # получив результат выходим из цикла
    
    return (count) 

random_number=np.random.randint(1, 101)   # создаем случайную переменную

min_score(random_number)  # запускаем функию              

def score_game(min_score) -> int:    
    runs=0 # число запусков
    count_ls=[] # список числа попыток
    count2=0 # сумма числа попыток
   
    while runs<1001:  
        runs+=1   
        count_ls.append(min_score(random_number)) # прибовляем число попыток в список числа попыток
    for number in count_ls:
        count2+=number  # складываем число попыток
        
    score=int(count2/1000) # среднее число попыток 
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    
    return score

score_game(min_score) # запускаем функцию
    
                


