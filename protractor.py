def solution(angle):
    0 < int(angle) <= 180
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    else:
        return 4
    
solution(70)
solution(92)
solution(180)