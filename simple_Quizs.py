# 두 정수 사이의 합

def solution(a, b):
    answer = 0
    if b > a:
        while a <= b:
            answer += a
            a += 1
        return answer
    elif b < a:
        while b <= a:
            answer += b
            b += 1
        return answer
    else:
        return a


first_num = int(input("정수를 입력하세요 :"))
sec_num = int(input("또 정수를 입력하세요 :"))
print("두 정수의 합은 {}입니다!!!".format(solution(first_num, sec_num)))