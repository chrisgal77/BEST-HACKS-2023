from googletrans import Translator


class PolishEnglishTranslator:
    model = Translator()

    def translate2english(self, text: str) -> str:
        return self.model.translate(text, dest="en").text
    
    def translate2polish(self, text: str) -> str:
        return self.model.translate(text, dest="pl").text

model = PolishEnglishTranslator()
