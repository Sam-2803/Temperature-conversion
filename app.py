from dotenv import load_dotenv
import os
load_dotenv()
api_key= os.getenv("OPEN_AI_API")
print(api_key)

print("hello")