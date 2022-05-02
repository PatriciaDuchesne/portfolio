MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}

user_text = input("What do you wish to translate? ").upper()


def translate_to_morse(text):
    translated_text = ""
    for letter in text:
        if letter == " ":
            translated_text = translated_text + "       "
        elif letter in MORSE_CODE:
            translated_text = translated_text + MORSE_CODE[letter] + "   "
        else:
            print(f"Character '{letter}' cannot be translated in morse code. Please use only letters and numbers.")
            return
    return translated_text


print(translate_to_morse(text=user_text))
