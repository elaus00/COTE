def solution(wallpaper):
    # 리스트 컴프리헨션 활용. enumerate는 인덱스와 값을 동시에 반환
    coords = [(i, j) for i, row in enumerate(wallpaper) for j, ch in enumerate(row) if ch == "#"]
    rows, cols = zip(*coords)
    answer = [min(rows), min(cols), max(rows)+1, max(cols)+1]
    return answer