import requests
import os
from dotenv import load_dotenv
load_dotenv()
from gradio_client import Client

# API_URL = "https://api-inference.huggingface.co/models/google/gemma-2-2b"

# headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACEHUB_API_TOKEN')}"}

client = Client("huggingface-projects/gemma-2-2b-it", hf_token=os.getenv('HUGGINGFACEHUB_API_TOKEN'))

def ask_gemma2b(prompt):
	return client.predict(
			message=prompt,
			max_new_tokens=1024,
			temperature=0.6,
			top_p=0.9,
			top_k=50,
			repetition_penalty=1.2,
			api_name="/chat"
	)
