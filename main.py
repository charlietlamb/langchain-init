import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from typing import Optional
from pydantic import BaseModel, Field

load_dotenv()

openai_api_key = os.environ.get("OPENAI_API_KEY")

model = init_chat_model("gpt-4o-mini", model_provider="openai")

class Joke(BaseModel):
    """Joke to tell user."""

    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline to the joke")
    rating: Optional[int] = Field(
        default=None, description="How funny the joke is, from 1 to 10"
    )
    
structured_llm = model.with_structured_output(Joke)

output = structured_llm.invoke("Tell me a joke about cats")

print(output)
