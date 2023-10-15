#6.write a function to find sum of given values,
#pass values has variable number of arguments to function.

def find_sum(*args):
    total = 0
    for num in args:
        total += num
    return total
result = find_sum(1, 2, 3, 4, 5)
print("sum:", result)


def summ(num1, *args):
    total = num1
    for num in args:
        total = total + num
    return total
result = summ(1, 2, 3, 4, 5, 6, 7,)
print("sum:", result)