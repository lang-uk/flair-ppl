import sys
import csv
import argparse
from hashlib import sha1
from pathlib import Path
from tqdm import tqdm
from flair.models.language_model import LanguageModel

if __name__ == "__main__":
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Calculate and export ppl for each sentence in the corpus using flair model"
    )

    parser.add_argument("embeddings", type=Path, help="Input file with forward flair embeddings")
    parser.add_argument(
        "infile",
        help="Input corpus with one sentence per line",
        nargs="?",
        type=argparse.FileType("r"),
        default="bruk.sentences.combined.txt",
    )
    parser.add_argument(
        "outfile",
        nargs="?",
        type=argparse.FileType("w"),
        default=sys.stdout,
        help="Output csv file with sentences and perplexity",
    )

    args: argparse.Namespace = parser.parse_args()
    lm: LanguageModel = LanguageModel.load_language_model(args.embeddings)

    w = csv.DictWriter(args.outfile, fieldnames=["id", "sentence", "ppl", "sentence_len"])
    w.writeheader()

    for i, sentence in enumerate(tqdm(map(str.strip, args.infile))):
        if not sentence:
            continue
        try:
            w.writerow(
                {
                    "id": sha1(sentence.encode("utf-8")).hexdigest(),
                    "sentence": sentence,
                    "ppl": lm.calculate_perplexity(sentence),
                    "sentence_len": len(sentence),
                }
            )
        except Exception:
            print("WTF", i, sentence)
