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

def solution_01_1(numbers_01_1):
    answer_01_1 = []
    for num_01_1 in numbers_01_1:
        for num_02_1 in numbers_01_1:
            if num_01_1 != num_02_1:
                sum_nums_1 = num_01_1 + num_02_1
                if sum_nums_1 not in answer_01_1 :
                    answer_01_1.append(sum_nums_1)
    return sorted(answer_01_1)


print(solution_01_1([2,1,3,4,1])) # 1+1이 다른요소임에도 불구 하고 2가 출력이 안됨, 틀린답




# 두 정수의 합에서 나올수있는 값을 모두 정리한 리스트(정답)

def solution_01(numbers_01):
    answer_01 = []
    for i in range(len(numbers_01)):
        for j in range(len(numbers_01)):
            if i != j:
                sum_nums = numbers_01[i] + numbers_01[j]
                if sum_nums not in answer_01:
                    answer_01.append(sum_nums)
    return sorted(answer_01)

print(solution_01([2,1,3,4,1])) #result [2,3,4,5,6,7]
print(solution_01([5,0,2,7])) #result [2,5,7,9,12]


# 같은숫자는 싫어(오답: 반복되는 숫자가 뒤쪽에 다시나올떄는 출력해야하는데,,, 이 코드는 안됨)

def solution_02_1(arr):
    answer_02_1 = []
    for factor_1 in arr:
        if factor_1 not in answer_02_1:
            answer_02_1.append(factor_1)
    return answer_02_1

print(solution_02_1([1,1,3,3,0,1,1]))   #result [1, 3, 0] but i want to get [1,3,0,1]

# 같은숫자는 싫어 (정답)

def solution_02(arr):
    answer_02 = []
    for factor in arr:
        if factor not in answer_02:
            answer_02.append(factor)
        elif factor != answer_02[-1]:
            answer_02.append(factor)
    return answer_02

print(solution_02([1,1,3,3,0,1,1])) # result [1, 3, 0, 1]
print(solution_02([4,4,4,3,3])) # result [4, 3]
print(solution_02([4,7,7,4,4,4,3,3,5,3])) # result [4, 7, 4, 3, 5, 3]


