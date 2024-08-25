import sys
from ft_filter import ft_filter


def main():
    """
    Filters words in a string based on their length.

    Arguments:
    - string (str): The text string.
    - n (int): Minimum length of the words to include in the result.

    Returns:
    - list: List of words that are more than 'n' characters long.
    """

    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        n = int(sys.argv[2])

        if not isinstance(text, str) or not isinstance(n, int):
            raise AssertionError("the arguments are bad")

        filtered_words = \
            list(ft_filter(lambda word: len(word) > n, text.split()))

        print(filtered_words)

    except ValueError as error:
        print("ValueError:", error)
    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()
