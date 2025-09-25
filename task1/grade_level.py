def coleman_liau_index(text):
    letters = 0
    for char in text:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            letters += 1

    words = len(text.split())
    sentences = sum(text.count(c) for c in '.!?')

    L = (letters / words) * 100
    S = (sentences / words) * 100

    index = 0.0588 * L - 0.296 * S - 15.8
    return round(index)

# Example usage
text = input("Enter the text: ")
grade = coleman_liau_index(text)

if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print("Grade", grade)