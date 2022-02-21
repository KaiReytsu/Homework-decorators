# Добавьте к первому заданию возможность передавать
# границы диапазона для поиска всех простых чисел
import time

def stopwatch(func):
    def wrap(*args):
        start = time.time()
        result = func(*args)
        return time.time() - start, result
    return wrap

@stopwatch
def prime_numbers(one, two):
    '''Return prime numbers of the list'''
    list_num = range(one, two + 1)
    prime_list = []
    start_seq = 2
    for num in list_num:
        if all(num % seq != 0 for seq in range(start_seq, num)):
            prime_list.append(num)
    return prime_list

sec, res = prime_numbers(1, 1000)
print('Seconds: {sec}\nResult: {res}'.format(sec = sec, res = res))