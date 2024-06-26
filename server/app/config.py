import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_VERSION = '/api'
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_JWT = os.getenv('SUPABASE_JWT')
    SUPABASE_ANON = os.getenv('SUPABASE_ANON')
    LLAMA_API= os.getenv('LLAMA_API')
    LLAMA_PARSER= os.getenv('LLAMA_PARSE')
    SUPABASE_KEY= os.getenv('SUPABASE_KEY')
