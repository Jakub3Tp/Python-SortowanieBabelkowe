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

if __name__ == '__main__':
    numbers1 = rand_number(10)
    bubble_sort(numbers1)
    numbers2 = rand_number(10)
    choice_sort(numbers2)
    numbers3 = rand_number(10)
    insertion_sort(numbers3)
    show(numbers1)
    show(numbers2)
    show(numbers3)

