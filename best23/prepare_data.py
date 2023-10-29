from pathlib import Path
import click
from tqdm.auto import tqdm
import json

from best23.models.text_embeddings import model as EMBEDDER


def process_data(input_file: str):

    data_path = Path(input_file)

    with open(input_file, "r") as in_file:
        all_data = json.load(in_file)

    output_data = {}

    for category, data in tqdm(all_data.items()):
        output_data[category] = []
        for item in data:
            temp = {}
            for key, value in item.items():

                temp[key] = value
                if key == "description":
                    temp["embedding"] = EMBEDDER.create_bert_embeddings(
                        value
                    ).tolist()
            output_data[category].append(temp)

    with open(data_path.parent / f"{data_path.stem}_processed.json", "w") as out_file:
        json.dump(output_data, out_file, indent=4)


@click.command()
@click.option("--input-file", required=True, type=str)
def main(input_file: str):
    process_data(input_file=input_file)

if __name__ == "__main__":
    main()