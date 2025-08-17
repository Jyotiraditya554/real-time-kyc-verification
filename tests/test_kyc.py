from src.kyc_verification import verify_kyc

def test_verified():
    features = {"tfidf_score": 0.8}
    result = verify_kyc(features)
    assert result["status"] == "Verified"

def test_rejected():
    features = {"tfidf_score": 0.3}
    result = verify_kyc(features)
    assert result["status"] == "Rejected"
