from langchain_google_genai import GoogleGenerativeAIEmbeddings
from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

text = "Hello world"
GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

result = embeddings.embed_documents(
    "hello world"
)

print(result)