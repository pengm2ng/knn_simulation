import math

def euclidean(a,b):
    x = b[0] - a[0]  # 선 a의 길이
    y = b[1] - a[1]  # 선 b의 길이

    dist = math.sqrt((x * x) + (y * y))  # (a * a) + (b * b)의 제곱근을 구함
    return dist