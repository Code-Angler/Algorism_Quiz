# 문제 설명
# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.
#
# 제한 조건
# num은 int 범위의 정수입니다.
# 0은 짝수입니다.

def solution(num):
    if num % 2 == 1:
        return 'Odd'
    else:
        return 'Even'
    return answer


# 직사각형 별찍기

# 문제 설명
# 이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
# 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.


# 내가 푼 풀이

def solution(a,b):
    rec = ''
    width = '*' * a
    rectangle = (width + '\n') * b

    rec = rec + rectangle

    return rec

print(solution(2, 3))


# map을 이욯한 풀이법(풀이 참조-1)

a, b = map(int, input().strip().split(' '))
width = '*' * a
rectangle = (width + '\n') * b
print(rectangle)


# map을 이용한 풀이법(플이 참조 -2)
a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print('*',end='')
    print('')

# map을 이용한 풀이법(플이 참조 -3)

a, b = map(int, input().strip().split(' '))
for i in range(b):
    print("*"*a)


