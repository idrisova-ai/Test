numbers = input().split(" ")
a = int(numbers[0])
b = int(numbers[1])


def function(num1, num2):
    count = 0
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
        count += 1
    print(num1 or num2, count, end=' ')


function(a, b)
