# 두 정수 사이의 합

def solution(a, b):
    if a > b: a, b = b, a

    return sum(range(a,b+1))

first_num = int(input("정수를 입력하세요 :"))
sec_num = int(input("또 정수를 입력하세요 :"))
print("두 정수의 합은 {}입니다!!!".format(solution(first_num, sec_num)))