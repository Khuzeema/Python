# Function to convert integer to Roman Numerals
def int_to_roman(num):
    val = [
        1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
    ]
    syb = [
        'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

# Function to convert Roman Numeral to Integer
def roman_to_int(roman):
    roman_dict = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
        'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
        'V': 5, 'IV': 4, 'I': 1
    }
    num = 0
    i = 0
    while i < len(roman):
        # Check for two-character symbols like 'CM', 'IX', etc.
        if i + 1 < len(roman) and roman[i:i+2] in roman_dict:
            num += roman_dict[roman[i:i+2]]
            i += 2
        else:
            num += roman_dict[roman[i]]
            i += 1
    return num

# Main program with input handling
while True:
    print("\nChoose an option:")
    print("1. Convert Integer to Roman Numerals")
    print("2. Convert Roman Numerals to Integer")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        try:
            num = int(input("Enter an integer (1-3999): "))
            if 1 <= num <= 3999:
                print(f"Roman numeral: {int_to_roman(num)}")
            else:
                print("Please enter a number between 1 and 3999.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    elif choice == "2":
        roman = input("Enter a Roman numeral: ").upper()
        try:
            print(f"Integer: {roman_to_int(roman)}")
        except KeyError:
            print("Invalid Roman numeral. Please try again.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
