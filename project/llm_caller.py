import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class GroqService:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model_1 = self._get_secret("MODEL_1")

    @staticmethod
    def _get_secret(key, default=None):
        return os.getenv(key, default)

    def _get_completion(self, text: str, model_id: str) -> str:
        return self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": text},
            ],
            model=model_id,
        ).choices[0].message.content

    def run_prompt(self, text: str):
        prompt_1 = self._get_secret("RAW_TXT_PROMPT")
        yield self._get_completion(prompt_1.format(raw_text=text),
                                   model_id=self.model_1
                                   )

    def run_prompt_two(self, text: str):
        prompt_1 = self._get_secret("CONTENT_PROMPT")
        yield self._get_completion(prompt_1.format(summary_text=text),
                                   model_id=self.model_1
                                   )
