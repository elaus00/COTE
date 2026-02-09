#https://school.programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    answer = []
    di = {} 
    # 이 딕셔너리에 장르(키), [장르별 총 플레이수, [노래 플레이수,인덱스],...](밸류) 형태로 넣음 
    
    for i in range(len(genres)):
        g, p = genres[i], plays[i]
        if g not in di:
            di[g] = [0, []]
        di[g][0] += p #장르별 총 플레이수 구하기 위해서 더함
        di[g][1].append((p, i)) #각 노래 플레이수랑 인덱스 추가 
    # 장르별 총 플레이수 기준으로 내림차순 정렬
    sorted_di = sorted(di.items(), key=lambda x: x[1][0], reverse=True)
    
    for genre, data in sorted_di:
         # 플레이수는 내림차순, 인덱스는 오름차순 정렬
        songs = sorted(data[1], key=lambda x: (-x[0], x[1])) 
        for s in songs[:2]: # [플레이수, 인덱스] 형태
            answer.append(s[1]) #인덱스만 정답에 추가
    
        
            
    return answer