a = int(input())
b = int(input())
c = int(input())

numbers = [a, b, c]

count_a = numbers.count(a)
count_b = numbers.count(b)
count_c = numbers.count(c)

max_count = max(count_a, count_b, count_c)

print(max_count)
