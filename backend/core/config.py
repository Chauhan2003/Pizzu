from dotenv import load_dotenv
import os

load_dotenv()

# Load environment variables
API_PREFIX = os.getenv("API_PREFIX", "/api/v1")
DATABASE_URL = os.getenv("DATABASE_URL")

