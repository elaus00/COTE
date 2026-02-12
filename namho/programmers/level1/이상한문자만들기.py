#https://school.programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    answer = []
    words = s.split(' ') #공백이 여러개 입력 가능하므로 split() 아니라 split(' ') 
    for word in words:
        w = ''
        for i in range(len(word)):
            if i%2 == 0:
                w+=word[i].upper()
            else:
                w+=word[i].lower()
        answer.append(w)
        
    return ' '.join(answer) #사이에 공백 두고 조인