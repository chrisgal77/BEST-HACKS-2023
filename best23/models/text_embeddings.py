import torch
from transformers import BertTokenizer, BertModel
import numpy as np
from keybert import KeyBERT


class TextEmbedder:
    model = BertModel.from_pretrained("dkleczek/bert-base-polish-cased-v1")
    tokenizer = BertTokenizer.from_pretrained("dkleczek/bert-base-polish-cased-v1")
    keyword_extractor = KeyBERT()

    def create_bert_embeddings(self, text: str) -> np.ndarray:
        keywords = [keywords for keywords, _ in self.keyword_extractor.extract_keywords(text, keyphrase_ngram_range=(1, 2))][:3]

        embeddings = []
        for keyword in keywords:
            tokens = self.tokenizer(keyword, padding=True, truncation=True, return_tensors='pt')

            with torch.no_grad():
                model_output = self.model(**tokens)

            embeddings.append(model_output.last_hidden_state.mean(dim=1).squeeze().numpy())

        return np.stack(embeddings).mean(axis=0)

model = TextEmbedder()