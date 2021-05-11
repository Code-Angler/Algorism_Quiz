# 문제 설명
# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# n은 1 이상 100,000,000 이하인 자연수입니다.

# 내가 푼 3진법 풀이

def solution(n):
    answer = 0
    rev_thr = []
    z = 1
    for i in range(1, 100):
        if (3 ** i) < n:
            a = (n // (3 ** (i-1)))
            thr = a % 3
            rev_thr.append(thr)
            if a < 9:
                rev_thr.append(a // (3))

    for j in rev_thr:
        number = ((3 ** (len(rev_thr)-z) * j))
        z += 1
        answer += number
    return answer

print(solution(45))  # result 7 ,rev_thr = [0,0,2,1]
print(solution(125)) # result 229, rev_thr = [2,2,1,1,1]


# 삼진법  (divmod)이용


def solution(n):
    rev_ternary = ''
    answer = 0
    j = 1

    while n > 0:
        n, mod = divmod(n, 3)
        rev_ternary += str(mod)

    for i in rev_ternary:
        number = ((3 ** (len(rev_ternary) - j) * int(i)))
        j += 1
        answer += number
    return answer

print(solution(45))  # result 7 ,rev_thr = [0,0,2,1]
print(solution(125)) # result 229, rev_thr = [2,2,1,1,1]


# 3진법 초간단 답 ( 풀이참조 **int )

def solution(n):
    rev_ternary = ''
    while n:
        rev_ternary += str(n % 3)
        n = n // 3

    answer = int(rev_ternary,3)
    return answer

print(solution(45))  # result 7 ,rev_thr = [0,0,2,1]
print(solution(125)) # result 229, rev_thr = [2,2,1,1,1]


# 문자열 다루기 기본

# 문제 설명
# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

# 제한 사항
# s는 길이 1 이상, 길이 8 이하인 문자열입니다.

def solution(s):
    answer = True
    if s.isdigit() and ((len(s) == 4) or(len(s)) == 6):
        return answer
    else:
        return False

print(solution("a234")) # result False
print(solution("1234")) # result True




# 제일 작은 수 제거하기
#
# 문제 설명
# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.
#
# 제한 조건
# arr은 길이 1 이상인 배열입니다.
# 인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.

def solution(arr):
    if 1 < len(arr):
        index_min_num = arr.index(min(arr))
        arr.pop(index_min_num)
        return arr
    else:
        return [-1]

print(solution([4, 3, 2, 1])) # result [4, 3, 2]
print(solution([-10])) # result [-1]



