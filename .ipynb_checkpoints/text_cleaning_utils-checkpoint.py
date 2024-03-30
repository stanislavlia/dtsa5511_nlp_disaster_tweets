
import re
import spacy
import string


def remove_url(text):
 return re.sub(r'https?:\S*', '<URL>', text)

def remove_mentions_and_tags(text):
    text = re.sub(r'@\S*', '', text)
    return re.sub(r'#\S*', '', text)


def remove_special_characters(text):
    # define the pattern to keep
    pat = r'[^a-zA-z0-9.,!?/:;\"\'\s]' 
    return re.sub(pat, '', text)


def remove_numbers(text):
    pattern = r'[^a-zA-z.,!?/:;\"\'\s]' 
    return re.sub(pattern, '', text)

def remove_punctuation(text):
    return ''.join([c for c in text if c not in string.punctuation])



def clean_text(text):

    lowered_text = text.lower()
    removed_tags_text = remove_mentions_and_tags(lowered_text)
    removed_urls_text = remove_url(removed_tags_text)
    removed_spec_chars_text = remove_special_characters(removed_urls_text)
    removed_numbers_text = remove_numbers(removed_spec_chars_text)

    cleaned_text = remove_punctuation(removed_numbers_text).strip()

    return cleaned_text
    

