from backend import create_app
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create the Flask instance
app = create_app()

# Vercel handles the 'run' command, so we only need this for local testing
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)