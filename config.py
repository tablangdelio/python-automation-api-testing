import os
from dotenv import load_dotenv


class EnvConfig:
    load_dotenv()
    API_URL: str = os.getenv("API_URL")
   
