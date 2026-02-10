def solution(n, w, num):
    total_rows = ((n + w - 1) // w)
    row = (num - 1) // w + 1
    order = 0

    # order 구하기
    if (row % 2 == 0):
        order = w - ((num - 1) % w + 1)
    else:
        order = (num - 1) % w

        # 꼭대기 층수의 order 구하기
    if n % w == 0:
        answer = total_rows - (row - 1)
    elif (total_rows % 2 == 0):
        if ((w - n % w) > order):
            answer = total_rows - row
        else:
            answer = total_rows - (row - 1)
    else:
        if (n % w > order):
            answer = total_rows - (row - 1)
        else:
            answer = total_rows - row
    return answer