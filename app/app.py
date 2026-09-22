import serpapi
import os
from dotenv import load_dotenv

load_dotenv()

client = serpapi.Client(api_key=os.getenv("SERP_API_KEY"))
results = client.search({
  "q": "fraud",
  "location": "india",
  "hl": "en",
  "gl": "us",
  "domain": "google.com"
})

print(results)
