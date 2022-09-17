"""Balcony models utils."""

import string
import re


def drop_spam_rows(text_series, spam_messages):
    """Remove rows containing spam messages from the provided series."""
    return text_series[text_series.str.contains('|'.join(spam_messages)) == False]

def remove_digits(text):
    """Remove digits from text."""
    dictionary = str.maketrans("", "", string.digits)
    return text.translate(dictionary)

def remove_prefixed_words(prefix, text):
    """Remove words with specific prefixes from text."""
    return re.sub(f"{prefix}[^, ]*", "", text)

def remove_single_characters(text):
    """Remove single characters from text."""
    return re.sub(r'\b\w\b', ' ', text)

def remove_special_characters(text):
    """Remove special characters from text."""
    return re.sub(r"\W", " ", text)

def contract_spaces(text):
    """Reduce multiple spaces to single space in text."""
    return re.sub(r"\s+", " ", text, flags=re.I)
