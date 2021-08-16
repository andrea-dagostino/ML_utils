import re
import nltk

def sanitize_text(text, remove_stopwords):
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