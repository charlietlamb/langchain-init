import weaviate
from weaviate.classes.init import Auth
from config import WCD_URL, WCD_API_URL, OPENAI_API_KEY

# Best practice: store your credentials in environment variables

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_URL,
    auth_credentials=Auth.api_key(WCD_API_URL),
    headers={"X-OpenAI-Api-key": OPENAI_API_KEY},
)
