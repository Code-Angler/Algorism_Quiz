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


# 두 정수의 합에서 나올수있는 값을 모두 정리한 리스트(오답)

def solution_1(numbers):
    answer = []
    for num_01 in numbers:
        for num_02 in numbers:
            if num_01 != num_02:
                sum_nums = num_01 + num_02
                if sum_nums not in answer:
                    answer.append(sum_nums)
    return sorted(answer)


print(solution_1([2, 1, 3, 4, 1]))  # result [3, 4, 5, 6, 7], 1+1이 다른요소임에도 불구 하고 2가 출력이 안됨, 틀린답


# 두 정수의 합에서 나올수있는 값을 모두 정리한 리스트(정답)


def solution_2(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                sum_nums = numbers[i] + numbers[j]
                if sum_nums not in answer:
                    answer.append(sum_nums)
    return sorted(answer)


print(solution_2([2, 1, 3, 4, 1]))  # result [2,3,4,5,6,7]
print(solution_2([5, 0, 2, 7]))  # result [2,5,7,9,12]


# 같은숫자는 싫어(오답: 반복되는 숫자가 뒤쪽에 다시나올떄는 출력해야하는데,,, 이 코드는 안됨)

def solution_01(arr):
    answer = []
    for factor in arr:
        if factor not in answer:
            answer.append(factor)
    return answer


print(solution_01([1, 1, 3, 3, 0, 1, 1]))  # result [1, 3, 0] but i want to get [1,3,0,1]


# 같은숫자는 싫어 (정답)

def solution_02(arr):
    answer = []
    for factor in arr:
        if factor not in answer:
            answer.append(factor)
        elif factor != answer[-1]:
            answer.append(factor)
    return answer


print(solution_02([1, 1, 3, 3, 0, 1, 1]))  # result [1, 3, 0, 1]
print(solution_02([4, 4, 4, 3, 3]))  # result [4, 3]
print(solution_02([4, 7, 7, 4, 4, 4, 3, 3, 5, 3]))  # result [4, 7, 4, 3, 5, 3]
