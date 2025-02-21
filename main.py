import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from typing import Optional
from typing_extensions import Annotated, TypedDict

load_dotenv()

openai_api_key = os.environ.get("OPENAI_API_KEY")

model = init_chat_model("gpt-4o-mini", model_provider="openai")

class Joke(TypedDict):
    """Joke to tell user."""

    setup: Annotated[str, ..., "The setup of the joke"] 
    punchline: Annotated[str, ..., "The punchline of the joke"]
    rating: Annotated[Optional[int], ..., "How funny the joke is, from 1 to 10"]
    
structured_llm = model.with_structured_output(Joke)

output = structured_llm.invoke("Tell me a joke about cats")

print(output)
