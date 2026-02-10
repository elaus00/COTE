#https://school.programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    citations.sort(reverse=True) #내림차순 정렬
    for i in range(len(citations)):
        # i번째 논문(인덱스 기준 i+1번째)이 i+1번 이상 인용되었는지 확인
        if citations[i] < i + 1:
            return i
            
    # 모든 논문이 전체 논문 수만큼 인용되었다면, 전체 논문 수가 답
    return len(citations)