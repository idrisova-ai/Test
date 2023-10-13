numbers = input().split(" ")
number = int(numbers[0])
count = int(numbers[1])

print(number & ((1 << count) - 1))
