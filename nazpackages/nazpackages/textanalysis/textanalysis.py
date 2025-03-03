def count_words(filepath, words_list):
    """
    Count the occurrences of specific words in a text file.

    This function reads a text file and counts how many times the words
    in the provided list appear in the file.

    Args:
        filepath (str): The path to the text file to be analyzed.
        words_list (list of str): A list of words to count occurrences of.

    Returns:
        int: The total number of times the words in `words_list` appear
        in the text file.
    """
    # Open the text file
    with open(filepath) as file:
        text = file.read()

    n = 0
    for word in text.split():
        # Count the number of times the words in the list appear
        if word.lower() in words_list:
            n += 1
    return n
