"""Игра угадай число.
компьютер сам загадывает и угадывает число."""
from numpy import imag, number


import numpy as np

def random_predict(number:int=1)->int:
    count=0
    
    while True:
        count+=1
        predict_number=np.random.randint(1,101)
        if number==predict_number:
            break
    return(count)

print(f"количество попыток: {random_predict()}")    

def score_game(random_predict)->int:
    
    count_ls=[]
    np.random.seed(1)
    random_array=np.random.randint(1,101,size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score=int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в средне за {score} попыток")
    return(score)

if __name__ =="_main_":
    score_game(random_predict) 