# 로또 번호 알고리즘

from random import randint

def generate_numbers(n):  # n개의 무작위한 번호를 추출하기 위한 함수
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)  # 1에서 45사이의 정수를 랜덤하게 뽑음
        if num not in numbers:
            numbers.append(num)

    return numbers

def draw_winning_numbers():  # 최종 당첨번호 7개 (6개의 무작위 넘버와 보너스번호)
    winning_nums = generate_numbers(7)
    return sorted(winning_nums[:6]) + winning_nums[6:]

def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for list_num in numbers:
        if list_num in winning_numbers:
            count += 1

    return count


def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

