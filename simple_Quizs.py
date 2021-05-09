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
#
# def solution_01(numbers_01):
#     answer_01 = []
#     for num_01 in numbers_01:
#         for num_02 in numbers_01:
#             if num_01 != num_02:
#                 sum_nums = num_01 + num_02
#                 if sum_nums not in answer_01 :
#                     answer_01.append(sum_nums)
#     return sorted(answer_01)
#
#
# print(solution_01([2,1,3,4,1])) # 1+1이 다른요소임에도 불구 하고 2가 출력이 안됨, 틀린답



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
