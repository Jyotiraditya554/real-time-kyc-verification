def verify_kyc(features):
    score = features.get("tfidf_score", 0)
    if score > 0.5:
        return {"status": "Verified", "score": score}
    else:
        return {"status": "Rejected", "score": score}
