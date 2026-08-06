from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()


class LLMService:

    def __init__(self):

        self.llm = ChatOpenAI(
            model="gpt-4.1-mini",
            temperature=0
        )

    def get_llm(self):

        return self.llm

    def ask(self, prompt: str):

        response = self.llm.invoke(
            [HumanMessage(content=prompt)]
        )

        return response.content