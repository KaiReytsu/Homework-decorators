# Создайте функцию, возвращающую список со всеми
# простыми числами от 0 до 1000.
# Используя механизм декораторов посчитайте 
# сколько секунд, потребовалось для вычисления всех простых чисел.
# Отобразите на экран количество секунд и простые числа
import time

def stopwatch(func):
    def wrap():
        start = time.time()
        result = func()
        return time.time() - start, result
    return wrap

@stopwatch
def prime_numbers():
    '''Return prime numbers of the list'''
    list_num = range(2, 1001)
    prime_list = []
    start_seq = 2
    for num in list_num:
        if all(num % seq != 0 for seq in range(start_seq, num)):
            prime_list.append(num)
    return prime_list

sec, res = prime_numbers()
print('Seconds: {sec}\nResult: {res}'.format(sec = sec, res = res))