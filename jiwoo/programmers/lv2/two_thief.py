# 다시 처음부터 풀어보기
def solution(info, n, m):
    items = len(info)
    INF = float('inf')
    dp = [INF] * n

    a_cost, b_cost = info[0]
    if a_cost < n:
        dp[a_cost] = 0
    if b_cost < m:
        dp[0] = b_cost

    for i in range(1, items):
        a_cost, b_cost = info[i]
        new_dp = [INF] * n

        for a in range(n):
            if dp[a] == INF:
                continue

            b = dp[a]

            # 선택1: A가 훔친다
            new_a = a + a_cost
            if new_a < n:
                new_dp[new_a] = min(new_dp[new_a], b)

            # 선택2: B가 훔친다
            new_b = b + b_cost
            if new_b < m:
                new_dp[a] = min(new_dp[a], new_b)

        dp = new_dp

    for a in range(n):
        if dp[a] < m:
            return a

    return -1