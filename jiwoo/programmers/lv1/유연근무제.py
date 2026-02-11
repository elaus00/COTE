def solution(schedules, timelogs, startday):
    answer = 0
    # 출근 희망 시각 순회 (직원 n명에 대해서)
    for i in range(len(schedules)):
        qualified = True

        # 각 시각의 충족 여부를 순회
        for j in range(len(timelogs[i])):
            # 주말 제외
            weekend = (startday + j) % 7
            if weekend == 0 or weekend == 6:
                continue
            # 마감 기준 설정
            deadline = schedules[i] + 10 if (schedules[i] % 100 + 10) < 60 else schedules[i] + 50
            qualified = True if timelogs[i][j] <= deadline else False
            if not qualified:
                break
        # 만약 i가 부합하는 경우 더하고, 그렇지 않은 경우 더하지 않기
        answer = answer + 1 if qualified else answer

    return answer

# 개선버전 (클로드 썜)
def solution1(schedules, timelogs, startday):
    def add_minutes(time, minutes):
        h, m = divmod(time, 100)
        total = h * 60 + m + minutes
        return (total // 60) * 100 + total % 60

    def is_weekday(day_index):
        return (startday + day_index) % 7 not in (0, 6)

    return sum(
        all(
            log <= add_minutes(schedule, 10)
            for day, log in enumerate(logs)
            if is_weekday(day)
        )
        for schedule, logs in zip(schedules, timelogs)
    )