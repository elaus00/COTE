#https://school.programmers.co.kr/learn/courses/30/lessons/340212
def solution(diffs, times, limit):
    # 1. 소요 시간 계산 함수 (숙련도가 level일 때)
    def cal_time(level):
        # 첫 번째 퍼즐은 난이도와 상관없이 항상 times[0]만큼 걸림
        total_time = times[0] 
        
        for i in range(1, len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = times[i-1]
            
            if diff <= level:
                # 내 숙련도가 높으면 한 번에 해결
                total_time += time_cur
            else:
                # 내 숙련도가 낮으면 실수 발생
                # 실수 횟수 = (난이도 - 숙련도)
                # 한 번 실수할 때마다 (현재 시간 + 이전 시간) 소요
                # 마지막에 성공할 때 현재 시간(time_cur) 추가
                num_fail = diff - level
                total_time += num_fail * (time_cur + time_prev) + time_cur
                
            # 계산 도중 이미 limit을 넘었다면 바로 끝
            if total_time > limit:
                return total_time
        return total_time

    # 이분 탐색 설정
    low = 1
    high = max(diffs)
    answer = high # 최악의 경우 가장 높은 난이도로 초기화

    while low <= high:
        mid = (low + high) // 2 # 현재 테스트할 숙련도
        
        if cal_time(mid) <= limit:
            # 제한 시간 내에 통과했으면 더 낮은 숙련도로도 가능한지 확인하기 위해 왼쪽 탐색
            answer = mid
            high = mid - 1
        else:
            # 시간을 초과하면 숙련도를 높여야 하므로 오른쪽 탐색
            low = mid + 1
            
    return answer