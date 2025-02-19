import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")


model = init_chat_model("gpt-4o-mini", model_provider="openai")
