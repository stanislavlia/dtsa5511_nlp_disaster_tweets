
import re
import string
import nltk
from nltk.corpus import stopwords


def remove_url(text):
 return re.sub(r'https?:\S*', '', text)

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

def remove_stopwords(text):
    stop_words = set(stopwords.words('english')) + set("qwertyiopasdfghjklzxcvbnm")
    return ' '.join([word for word in text.split() if word.lower() not in stop_words])



def clean_text(text):

    lowered_text = text.lower()
    removed_tags_text = remove_mentions_and_tags(lowered_text)
    removed_urls_text = remove_url(removed_tags_text)
    removed_spec_chars_text = remove_special_characters(removed_urls_text)
    removed_numbers_text = remove_numbers(removed_spec_chars_text)

    cleaned_text = remove_stopwords(remove_punctuation(removed_numbers_text).strip())

    return cleaned_text
    

