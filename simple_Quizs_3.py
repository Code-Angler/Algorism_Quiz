# 비밀지도

def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        bin_1 = int(bin(i)[2:])
        bin_2 = int(bin(j)[2:])
        sum_bin = str(bin_1 + bin_2)
        if len(sum_bin) < n:
            sum_bin = (('0'*(n-(len(sum_bin)))) + sum_bin)
        final = ''
        for k in range(n):
            if sum_bin[k] == '0':
                final += ' '
            else:
                final += '#'
        answer.append(final)
    return answer

print((solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])))


# 음양 더하기

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] :
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

print(solution([4,7,12],[True,False,True]))

# 이상한 문자 만들기(테스트에서 실패, but it is working!!)

def solution(s):
    answer = ''
    sprate_words = s.split(" ")
    for word in sprate_words:
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i]
        answer += " "
    return answer[:-1]


print(solution("try hello world"))




