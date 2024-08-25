import sys


def encode_to_morse(text):
    """
    Encodes the given text into Morse code.

    Parameters:
    - text (str): The text to be encoded.

    Returns:
    - str: The Morse code representation of the input text.

    Raises:
    - AssertionError: If the input text contains characters
    not supported by Morse code.
    """

    NESTED_MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
    }

    morse_text = []
    for char in text.upper():
        if (char := NESTED_MORSE.get(char)) is not None:
            morse_text.append(char)
        else:
            raise AssertionError("the arguments are bad")
    return ' '.join(morse_text)


def main():
    try:
        if len(sys.argv) != 2 or len(sys.argv[1]) == 0 \
                or not isinstance(sys.argv[1], str):
            raise AssertionError("Usage: python3 sos.py <text>")
        input_text = sys.argv[1]
        morse_result = encode_to_morse(input_text)
        print(morse_result)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
