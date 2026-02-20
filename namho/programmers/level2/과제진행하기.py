#https://school.programmers.co.kr/learn/courses/30/lessons/176962
def solution(plans):
    plans = sorted([[p[0], int(p[1][:2]) * 60 + int(p[1][3:]), int(p[2])] for p in plans], key=lambda x: x[1])
    
    stop = []
    answer = []
    curr_time = 0

    for i in range(len(plans)):
        name, start, playtime = plans[i]
        
        # 새로운 과제를 시작하기 전, 멈춰둔 과제들을 처리할 여유 시간이 있는지 확인
        while stop and curr_time < start:
            s_name, s_remains = stop.pop()
            if curr_time + s_remains <= start: # 다 끝낼 수 있음
                curr_time += s_remains
                answer.append(s_name)
            else: # 다 못 끝냄
                stop.append([s_name, s_remains - (start - curr_time)])
                curr_time = start
        
        curr_time = start
        # 현재 과제를 일단 진행 (다음 과제가 있다면 그 전까지만)
        if i < len(plans) - 1:
            next_start = plans[i+1][1]
            if start + playtime <= next_start:
                answer.append(name)
                curr_time = start + playtime
            else:
                stop.append([name, playtime - (next_start - start)])
                curr_time = next_start
        else:
            # 마지막 과제는 무조건 끝남
            answer.append(name)

    # 모든 계획을 순회한 후 스택에 남은 것들 처리
    while stop:
        answer.append(stop.pop()[0])
        
    return answer