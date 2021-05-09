# 문제 설명
# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# n은 1 이상 100,000,000 이하인 자연수입니다.

def solution(n):
    rev_thr = []
    for i in range(1, 100):
        if (3 ** i) < n:
            a = (n // (3 ** (i-1)))
            thr = a % 3
            rev_thr.append(thr)
            if a < 9:
                rev_thr.append(a // (3))
    print(rev_thr)

    tenth = 0
    z = 1
    for j in rev_thr:
        number = ((3 ** (len(rev_thr)-z) * j))
        z += 1
        tenth += number
    print(tenth)

solution(45) # result 7 ,rev_thr = [0,0,2,1]
solution(125) # result 229, rev_thr = [2,2,1,1,1]
