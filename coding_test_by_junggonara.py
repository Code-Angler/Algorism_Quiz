# 수열을 어떠한 규칙에 의해 여러가지 항으로 나누었을때, 각각의 항으로 이루어진 수열을 군수열이라고 합니다.
# S ={1}, {1, 2}, {1, 2, 3}, {1, 2, 3, 4}......... 있을때 k 번째 수가 가리키는 값을 나타내는 함수를 완성하시오

def solution(k):

    i = 1
    cnt = 0
    answer = k
    while i < answer:
        cnt += 1
        answer = answer - i
        i += 1

    return answer

print(solution(100))




# n * m 직사각형에서 각 변은 x축 y축에 평행하며 해당 축의 좌표에 평행하게 잘랐을때 조각 중 가장 넓은 직사각형의 넓이를 구하시오.

def solution(n, m, x_axis, y_axis):
    answer = 0
    total = n * m

    x_list = x_axis
    x_list.append(n)
    y_list = y_axis
    y_list.append(m)


    while answer < total:
        x_spot = 0
        for x in x_list:
            y_spot = 0
            for y in y_list:
                width = (x - x_spot) * (y - y_spot)
                total -= width
                y_spot = y
                if answer < width:
                    answer = width
            x_spot = x

    return answer

print(solution(10, 10, [2, 6], [3, 7]))

# # 확인 하기위한 코드
#
# def solution(n, m, x_axis, y_axis):
#     answer = 0
#     total = n * m
#
#     x_list = x_axis
#     x_list.append(n)
#     y_list = y_axis
#     y_list.append(m)
#
#
#     while answer < total:
#         x_spot = 0
#         for x in x_list:
#             y_spot = 0
#             for y in y_list:
#                 width = (x - x_spot) * (y - y_spot)
#                 print(width)
#                 total -= width
#                 print(total)
#                 y_spot = y
#                 print(y_spot)
#                 if answer < width:
#                     answer = width
#                     print(answer)
#                 print("====================")
#             x_spot = x
#
#     return "answer" + str(answer)
#
# print(solution(10, 10, [2, 6], [3, 7]))




#  티켓팅시 [1, 2, 3, 3, 5, 6, 4, 3, 3, 2, 1] 이면 앞선 값을 제외한 해당번호를 정렬한 값 [1, 2, 3, 5, 6, 4]을 결과로 가지게하는 함수값을 완성하시오


#  결과값은 나오지만 효율성에서 부족함 70점/100점
def solution(waiting):
    answer = []

    for order in waiting:
        if order not in answer:
            answer.append(order)

    return answer



