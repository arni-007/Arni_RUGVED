def luhn_check(card_number):
    card_number = card_number.replace(" ", "")  # remove spaces
    if not card_number.isdigit():
        return False
    
    total = 0
    reverse_digits = card_number[::-1]
    
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:  # double every second digit from the right
            n = n * 2
            if n > 9:
                n -= 9
        total += n
    
    return total % 10 == 0

# Example usage
card = input("Enter credit card number: ")
if luhn_check(card):
    print("The credit card number is valid.")
else:
    print("The credit card number is invalid.")