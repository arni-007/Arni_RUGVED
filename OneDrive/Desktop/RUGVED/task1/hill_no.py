def is_hill_number(n):
    num_str = str(n)  
    if len(num_str) < 3:
        return False  

    i = 0

    while i < len(num_str) - 1 and num_str[i] < num_str[i + 1]:
        i += 1

    if i == 0 or i == len(num_str) - 1:
        return False
    
    while i < len(num_str) - 1 and num_str[i] > num_str[i + 1]:
        i += 1

    return i == len(num_str) - 1


num = int(input("Enter a number: "))
if is_hill_number(num):
    print(num, "is a hill number.")
else:
    print(num, "is not a hill number.")