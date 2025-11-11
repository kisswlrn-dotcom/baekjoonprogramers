def solution(a, b, flag):
    answer = 0
    if flag is True:
        answer = a + b
    elif flag is False:
        answer = a - b
    return answer