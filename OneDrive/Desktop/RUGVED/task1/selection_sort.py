def selection_sort_string(s):
    char_list = list(s)
    for i in range(len(char_list)):
        min_index = i
        for j in range(i + 1, len(char_list)):
            if char_list[j] < char_list[min_index]:
                min_index = j
        char_list[i], char_list[min_index] = char_list[min_index], char_list[i]
    sorted_str = ''.join(char_list)
    return sorted_str

text = input("Enter a string: ")
sorted_text = selection_sort_string(text)
print("Sorted String:", sorted_text)