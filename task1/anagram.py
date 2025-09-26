def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if is_anagram(s1, s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")