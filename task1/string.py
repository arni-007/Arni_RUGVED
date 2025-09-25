def sort_and_count(text):
    text = text.lower()
    
    sorted_str = ''.join(sorted(text))
    print("Sorted String:", sorted_str)

    print("\nCharacter Counts:")
    for char in sorted(set(sorted_str)):
        print(char, ":", sorted_str.count(char))


# Example usage
user_input = input("Enter a string: ")
sort_and_count(user_input)