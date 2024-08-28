# pip install retry python-dotenv 
import requests
import os
import pandas as pd
from dotenv import load_dotenv
from syllabi import syllabi

load_dotenv()

model_id = "sentence-transformers/all-MiniLM-L6-v2"

api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACEHUB_API_TOKEN')}"}

def query(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
    return response.json()

output = query(list(syllabi.values()))

embeddings = pd.DataFrame(output)
embeddings.to_csv("syllabi_embeddings.csv", index=False)

