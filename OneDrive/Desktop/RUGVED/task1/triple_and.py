def triple_and(a, b, c):
    return a and b and c

a = input("Enter first value (True/False): ") == "True"
b = input("Enter second value (True/False): ") == "True"
c = input("Enter third value (True/False): ") == "True"

print(triple_and(a, b, c))