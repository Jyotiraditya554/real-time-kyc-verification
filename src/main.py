from src.kyc_verification import verify_kyc
from src.text_extraction import extract_features
from src.langchain_integration import run_langchain
import os

def main():
    doc_path = os.path.join("data", "sample_docs", "sample.txt")
    
    # Step 1: Extract features from document
    features = extract_features(doc_path)
    
    # Step 2: Run KYC verification logic
    kyc_result = verify_kyc(features)
    
    # Step 3: Integrate with LLM via LangChain
    final_result = run_langchain(kyc_result)
    
    print("KYC Verification Result:", final_result)

if __name__ == "__main__":
    main()

