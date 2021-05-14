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