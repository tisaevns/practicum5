N, K, M = map(int, input().split())

result = min((M - K - 1) % N, (K - M - 1) % N)
print(result)
