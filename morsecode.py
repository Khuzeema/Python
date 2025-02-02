# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}

# Reverse Morse Code Dictionary for Decoding
REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

# Function to encode text to Morse code
def text_to_morse(text):
    text = text.upper()
    morse_code = ' '.join(MORSE_CODE_DICT[char] for char in text if char in MORSE_CODE_DICT)
    return morse_code

# Function to decode Morse code to text
def morse_to_text(morse):
    text = ''.join(REVERSE_MORSE_CODE_DICT[char] for char in morse.split(' ') if char in REVERSE_MORSE_CODE_DICT)
    return text

# Menu for the converter
def main():
    print("Morse Code Converter")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        text = input("Enter text to convert to Morse code: ")
        print("Morse Code:", text_to_morse(text))
    elif choice == '2':
        morse = input("Enter Morse code to convert to text (use spaces to separate): ")
        print("Text:", morse_to_text(morse))
    else:
        print("Invalid choice! Please select 1 or 2.")

if __name__ == "__main__":
    main()
