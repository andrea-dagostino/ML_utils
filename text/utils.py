import re
import nltk

def sanitize_text(text: str, remove_stopwords: bool) -> str:
    """ This utility function sanitizes a string by:
    - removing links
    - removing special characters
    - removing numbers
    - removing stopwords
    - transforming in lowercase
    - removing excessive whitespaces

    Args:
        text (str): the input text you want to clean
        remove_stopwords (bool): whether or not to remove stopwords

    Returns:
        str: the cleaned text
    """
    
    # remove links
    text = re.sub(r'http\S+', '', text)
    # remove special chars and numbers
    text = re.sub('[^A-Za-z]+', ' ', text)
    # remove stopwords
    if remove_stopwords:
        # 1. tokenize
        tokens = nltk.word_tokenize(text)
        # 2. check if stopword
        tokens = [w for w in tokens if not w.lower() in STOPWORDS]
        # 3. join back together
        text = " ".join(tokens)
    # return text in lower case and stripped of whitespaces
    text = text.lower().strip()
    
    return text

def remove_punctuation(text):
    punctuation_free = "".join([i for i in text if i not in string.punctuation])
    return punctuation_free

def remove_stopwords(text):
    output = [i for i in text if i not in STOPWORDS]
    return output