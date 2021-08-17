import re
import nltk


def sanitize_text(text: str, remove_stopwords: bool) -> str:
    """This utility function sanitizes a string by:
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
    text = re.sub(r"http\S+", "", text)
    # remove special chars and numbers
    text = re.sub("[^A-Za-z]+", " ", text)
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


def preprocess_text(text):
    text = text.lower()
    # remove hyperlinks
    text = re.sub(r"https?:\/\/.*[\r\n]*", "", text)
    text = re.sub(r"http?:\/\/.*[\r\n]*", "", text)
    # Replace &amp, &lt, &gt with &,<,> respectively
    text = text.replace(r"&amp;?", r"and")
    text = text.replace(r"&lt;", r"<")
    text = text.replace(r"&gt;", r">")
    # remove hashtag sign
    # text=re.sub(r"#","",text)
    # remove mentions
    text = re.sub(r"(?:\@)\w+", "", text)
    # text=re.sub(r"@","",text)
    # remove non ascii chars
    text = text.encode("ascii", errors="ignore").decode()
    # remove some puncts (except . ! ?)
    text = re.sub(r'[:"#$%&\*+,-/:;<=>@\\^_`{|}~]+', "", text)
    text = re.sub(r"[!]+", "!", text)
    text = re.sub(r"[?]+", "?", text)
    text = re.sub(r"[.]+", ".", text)
    text = re.sub(r"'", "", text)
    text = re.sub(r"\(", "", text)
    text = re.sub(r"\)", "", text)

    text = " ".join(text.split())
    return text


def remove_punctuation(text):
    punctuation_free = "".join([i for i in text if i not in string.punctuation])
    return punctuation_free


def remove_stopwords(text):
    output = [i for i in text if i not in STOPWORDS]
    return output


def lemmatize(text):
    tokens = nltk.word_tokenize(text)
    lemmatized_tokens = [wordnet_lemmatizer.lemmatize(word) for word in tokens]
    text = " ".join(lemmatized_tokens)
    return text


def stem(text):
    tokens = nltk.word_tokenize(text)
    stemmed_tokens = [porter_stemmer.stem(word) for word in tokens]
    text = " ".join(stemmed_tokens)
    return text


def stem_and_lemmatize(text):
    tokens = nltk.word_tokenize(text)
    stemmed_tokens = [porter_stemmer.stem(word) for word in tokens]
    lemmatized_tokens = [wordnet_lemmatizer.lemmatize(word) for word in stemmed_tokens]
    text = " ".join(lemmatized_tokens)
    return text
