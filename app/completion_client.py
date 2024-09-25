import openai

from config import prompt_path
from schemas import ResponseFormat


class CompletionClient:
    def __init__(self):
        self.client = openai.AsyncClient()
        self.prompt = self.get_prompt()

    @staticmethod
    def get_prompt() -> str:
        with open(prompt_path) as f:
            return f.read()

    async def get_completion(self, prompt) -> ResponseFormat | None:
        messages = [{"role": "user", "content": prompt}]
        response = await self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=messages,
            response_format=ResponseFormat,
        )
        message = response.choices[0].message
        if message.refusal:
            return None
        return message.parsed

    async def is_smart(self, task: str, goal: str) -> ResponseFormat | None:
        prompt = self.prompt.replace("{task}", task)
        prompt = prompt.replace("{goal}", goal)
        result = await self.get_completion(prompt)
        return result
