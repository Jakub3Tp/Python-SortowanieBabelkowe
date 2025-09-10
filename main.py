import math
import random


def rand_number(n: int) -> list:
    return [random.randint(1, 100) for _ in range(n)]

def show(numbers: list) -> None:
    for number in numbers:
        print(number, end=' ')
    print()

def bubble_sort(numbers: list) -> list:
    for j in range(len(numbers) - 1):
        for i in range(len(numbers) - 1 - j):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

def choice_sort(numbers: list) -> list:
    for j in range(len(numbers) - 1):
        pmin = numbers[j]
        for i in range(j + 1, len(numbers)):
            if numbers[i] < pmin:
                pmin = numbers[i]
        numbers[j], numbers[j + 1] = pmin, numbers[j]

def insertion_sort(numbers: list) -> list:
    for j in range(len(numbers) - 2, -1, -1):
        x = numbers[j]
        i = j + 1
        while i < len(numbers) and x > numbers[i]:
            numbers[i - 1] = numbers[i]
            i = i + 1
        numbers[i - 1] = x

def fusion(d: list, i_p, i_s, i_k):
    i_1 = i_p
    i_2 = i_s
    p = [0 for _ in range(len(d))]

    for i in range(i_p, i_k + 1):
        if (i_1 == i_s) or (i_2 >= i_k and d[i_1] > d[i_2]):
            p[i] = d[i_2]
            i_2 += 1
        else:
            p[i] = d[i_1]
            i_1 += 1

    for i in range(i_p, i_k + 1):
        d[i] = p[i]

def fusion_sort(d: list, i_p, i_k):
    i_s = (i_p + i_k - 1) // 2
    if i_s - i_p > 0:
        fusion_sort(d, i_p, i_s - 1)
    if i_k - i_s > 0:
        fusion_sort(d, i_s, i_k)
    fusion(d, i_p, i_s, i_k)

    return d

def searchingBinary(table: list[int], numbers: int) -> int:
    left, right = 0, len(table) - 1
    searcing_index = 0
    while left <= right:
        searcing_index = math.floor((left + right) / 2)
        if table[searcing_index] < numbers:
            left = searcing_index + 1
        elif table[searcing_index] > numbers:
            right = searcing_index - 1
        else:
            return searcing_index

    return None

def totalRoot(x: int) -> int:
    a = 0
    r1 = 1
    r2 = 2
    i = 0
    while a < x:
        a = a + r1
        r1 = r1 + r2
        i = i + 1
    return i - 1

def totalRoot2(x: int) -> int:
    if x > 1:
        p1 = 0
        p2 = x >> 1
        while abs(p1 - p2) > 1:
            p1 = p2
            p2 = (p2 + x // p1) >> 1
    else:
        p2 = x
        while (p2 * p2) > x:
            p2 = p2 - 1
    return p2
if __name__ == '__main__':
    #numbers1 = rand_number(10)
    #bubble_sort(numbers1)
    #numbers2 = rand_number(10)
    #choice_sort(numbers2)
    #numbers3 = rand_number(10)
    #insertion_sort(numbers3)
    #numbers4 = rand_number(10)
    #fusion_sort(numbers4, 0, 1)
    #show(numbers1)
    #show(numbers2)
    #show(numbers3)
    #list = [3, 4, 6, 5, 1, 10]
    #searchingBinary(list, 7)
    #show(list)
    #print(totalRoot(51))
    #print(math.sqrt(51))

    print(totalRoot2(51))
    print(math.sqrt(51))
