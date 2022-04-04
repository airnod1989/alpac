import numpy as np

number=np.random.randint(1,101)
count=0

while True:
    count+=1
    predict_number = int(input("угадай число 50"))
    
    if predict_number>number:
        print("меньше")
    elif predict_number<number:
        print("больше")
    else:
        print(f"Вы угадали число! Это число = {number} за {count} попыток!") 
        break       