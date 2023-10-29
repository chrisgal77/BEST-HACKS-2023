from langchain.llms import GooglePalm
import dataclasses

from pydantic import BaseSettings


class Palm2Config(BaseSettings):
    temperature: float = 0.1


PALM2_SETTINGS = Palm2Config()


@dataclasses.dataclass
class Palm2LLM:
    model = GooglePalm()

    def __post_init__(self):
        self.model.temperature = PALM2_SETTINGS.temperature

    def generate(self, text: str) -> str:
        results = self.model._generate([text])
        return results.generations[0][0].text


model = Palm2LLM()
