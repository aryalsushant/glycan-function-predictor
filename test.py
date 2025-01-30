from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Debug: Print loaded API key
print("Loaded API Key:", os.getenv("OPENAI_API_KEY"))
