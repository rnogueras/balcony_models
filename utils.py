"""Balcony models utils."""

import string
import re


def drop_spam_rows(text_series, spam_messages):
    return text_series[text_series.str.contains('|'.join(spam_messages)) == False]

def remove_digits(text):
    dictionary = str.maketrans("", "", string.digits)
    return text.translate(dictionary)

def remove_prefixed_words(prefix, text):
    return re.sub(f"{prefix}[^, ]*", "", text)

def remove_single_characters(text):
    return re.sub(r'\b\w\b', ' ', text)

def remove_special_characters(text):
    return re.sub(r"\W", " ", text)

def contract_spaces(text):
    return re.sub(r"\s+", " ", text, flags=re.I)

def remove_word(text, word):
    return re.sub(fr'\b{word}\b\s+',"", text)
    
