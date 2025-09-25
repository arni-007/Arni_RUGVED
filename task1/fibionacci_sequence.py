def fibonacci_sequence(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        count += 1

num = int(input("Enter the number of Fibonacci values: "))
fibonacci_sequence(num)