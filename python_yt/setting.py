import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
API_KEY = os.getenv("API_KEY") # 通常固定不變之參數以全大寫命名
