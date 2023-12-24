import math

def count_parking_permutations(N, A, B, C):
    result = math.comb(N, A) * math.comb(N - A, B) * math.comb(N - A - B, C)
    return result

N, A, B, C = map(int, input().split())

result = count_parking_permutations(N, A, B, C)
print(result)
