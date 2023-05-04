import numpy as np

def random_predict(number: int = 1) -> int:
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    
    return count

def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
def game_core_v3(number: int = 1) -> int:
    """Переделанный вариант с использованием бинарного поиска.  

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток.
    """
    count = 0
    predict = np.random.randint(1,101) #Стартовая точка угадывания.
    x = list(range(1,101)) #решил создать последовательность в виде списка равную радиусу угадываемых чисел.
    low = x[0] # Первый элемент - нижняя граница.
    high = len(x) # Длина списка - верхняя. 
    n = number #записал полученный number в n, для удобства.  
    while low <= high: #Бесконечный цикл.       
        count += 1 #При каждой итерации добавляет к числу попыток 1.       
        if predict < n: #Если число меньше загаданного, то приводит нижнюю границу к числу, а затем вычисляет среднее значение новой последовательности.  
            low = predict + 1
            predict = (high + low) // 2                     
        if predict > n: #Аналогично, если больше.           
            high = predict - 1
            predict = (high + low) // 2                       
        if predict == n: #Условие выхода из цикла, если число соответствует загаданному.                               
            break
    return count
            

         
        

#Эффективность всех алгоритмов.
print('Run benchmarking for random_predict: ', end='')
score_game(random_predict)

print('Run benchmarking for game_core_v2: ', end='')
score_game(game_core_v2)

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
        
    
            