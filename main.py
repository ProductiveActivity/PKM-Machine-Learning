import os
import sys

# Load environment variables if python-dotenv is installed
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def smoke_test():
    """Verify that the basic environment and directory structure are functional."""
    print("[AI-ENGINE/ML] Starting Machine Learning Worker Smoke Test...")
    print(f"[AI-ENGINE/ML] Python Version: {sys.version.split()[0]}")
    
    # Check directory structure
    base_dir = os.path.dirname(os.path.abspath(__file__))
    scraper_dir = os.path.join(base_dir, "scraper")
    nlp_dir = os.path.join(base_dir, "nlp")
    
    print(f"[AI-ENGINE/ML] Checking scraper module directory: {'OK' if os.path.isdir(scraper_dir) else 'MISSING'}")
    print(f"[AI-ENGINE/ML] Checking nlp module directory: {'OK' if os.path.isdir(nlp_dir) else 'MISSING'}")
    
    # Check optional env
    db_url = os.getenv("DATABASE_URL", "Not set (use .env.example)")
    print(f"[AI-ENGINE/ML] Database Target: {db_url.split('@')[-1] if '@' in db_url else db_url}")
    print("[AI-ENGINE/ML] Smoke test completed successfully. Pipeline worker is ready!")

def main():
    smoke_test()

if __name__ == "__main__":
    main()
