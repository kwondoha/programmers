def solution(line):
    pos, answer = [], []
    n = len(line)
    x_min = y_min = int(1e15)
    x_max = y_max = -int(1e15)
    
    for i in range(n):
        a,b,e = line[i]
        for j in range(i+1, n):
            c,d,f=line[j]
            if a*d == b*c : continue # 두 직선이 평행 또는 일치하면 패쓰
            
            x,y = (b*f - e*d) / (a*d - b*c), (e*c - a*f) / (a*d - b*c) # 공식 이용해서 교점 x,y 구하기
            
            if x==int(x) and y==int(y) : #정수 교점이라면
                x,y = int(x),int(y)
                pos.append([x,y]) # 교점 저장
                if x_min > x : x_min = x # 교점 표현을 위한 최소한의 사각형 구하기
                if y_min > y : y_min = y
                if x_max < x : x_max = x
                if y_max < y : y_max = y
                
    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    box = [['.'] * x_len for _ in range(y_len)]

    for sx, sy in pos:
        nx = sx + abs(x_min) if x_min < 0 else sx - x_min
        ny = sy + abs(y_min) if y_min < 0 else sy - y_min
        box[ny][nx] = '*'
    for result in box : answer.append(''.join(result))
    return answer[::-1]