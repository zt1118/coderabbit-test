# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Return the characters of a string in reverse order.
    
    Returns:
        str: The input string with characters reversed.
    """
    return text[::-1]

def count_words(sentence):
    """
    Count the number of words in a sentence.
    
    Parameters:
        sentence (str): Input text whose words will be counted; words are delimited by whitespace.
    
    Returns:
        int: Number of words in the given sentence.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.
    
    Parameters:
        celsius (float | int): Temperature in degrees Celsius.
    
    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32
