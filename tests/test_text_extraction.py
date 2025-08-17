from src.text_extraction import extract_features

def test_extraction():
    features = extract_features("data/sample_docs/sample.txt")
    assert "tfidf" in features
    assert features["tfidf_score"] > 0
