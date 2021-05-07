#로또 번호 알고리즘

from random import randint

def generate_number(n): # n개의 무작위한 번호를 추출하기 위한 함수
    lucky_nums = []

    while len(lucky_nums) < n:
        lucky = randint(1, 45) # 1에서 45사이의 정수를 랜덤하게 뽑음
        if lucky not in lucky_nums:
            lucky_nums.append(lucky)

    return lucky_nums


def draw_winning_numbers(): # 최종 당첨번호 7개 (6개의 무작위 넘버와 보너스번호)
    winning_nums = generate_number(7)
    print(sorted(winning_nums[:6]) + winning_nums[6:])


draw_winning_numbers()



