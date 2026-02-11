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

# 개선 버전 (with AI)
def solution1(n, w, num):
    total_rows = (n + w - 1) // w
    row = (num - 1) // w
    pos = (num - 1) % w
    order = (w - 1 - pos) if row % 2 else pos

    top_row = total_rows - 1
    top_count = n - top_row * w  # 꼭대기 층 상자 수
    top_pos = (w - 1 - order) if top_row % 2 else order

    covered = top_pos < top_count
    return total_rows - row if covered else total_rows - row - 1
