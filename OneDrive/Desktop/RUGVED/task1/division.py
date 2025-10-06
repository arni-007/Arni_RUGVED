def divide_string(s, n):
    if len(s) % n != 0:
        print("Error: The string cannot be divided into equal parts of length", n)
        return
    
    parts = [s[i:i+n] for i in range(0, len(s), n)]
    

    if all(part == parts[0] for part in parts):
        print("Divided parts:", ', '.join(parts))
    else:
        print("Error: Parts are not identical.")

string = input("Enter the string: ")
n = int(input("Enter the length of each part: "))
divide_string(string, n)