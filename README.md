# A tool to calculate perplexity of a flair vectors on Brown-UK corpus

## Usage
 - Install deps: `pip install flair`
 - Clone or update the BRUK: `git clone https://github.com/brown-uk/corpus.git`
 - Combine all texts into one: `python prepare_corpus.py "corpus/data/good/*.txt" > /tmp/bruk.paras.combined.txt`
 - Tokenize it with [NLP-uk lib](https://github.com/brown-uk/nlp_uk):
 `cat /tmp/bruk.paras.combined.txt | pv -cN "Input" | groovy TokenizeText.groovy -s -i - -o - | pv -cN "Output" > /tmp/bruk.sentences.combined.txt`
 - Download or clone flair embeddings, for example, [from here](https://huggingface.co/dchaplinsky/flair-uk-forward).
 - Calculate perplexity on the corpus `python calculate_ppl.py ../flair-uk-forward/best-lm.pt /tmp/bruk.sentences.combined.txt  /tmp/flair-uk-forward.ppl.csv`
 
 enjoy.
