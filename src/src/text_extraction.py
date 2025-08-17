from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def extract_features(file_path):
    with open(file_path, "r") as f:
        text = f.read()
    
    # Bag of Words
    vectorizer = CountVectorizer()
    bow = vectorizer.fit_transform([text])
    
    # TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    tfidf = tfidf_vectorizer.fit_transform([text])
    
    tfidf_score = tfidf.sum() / tfidf.shape[1]
    
    return {"bow": bow, "tfidf": tfidf, "tfidf_score": tfidf_score}
