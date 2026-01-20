from backend import create_app
from dotenv import load_dotenv
import os

# 1. Load env vars
load_dotenv()

# 2. Vercel MUST see a variable named 'app' in this file
app = create_app()

# This part is ignored by Vercel but kept for local testing
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)