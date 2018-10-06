import sys
import fastText as ft
import MeCab
import re
import datetime

now = datetime.datetime.today().strftime("%m%d_%H%M")

MODEL_FILE = "../bin/model1006_1925.bin"
TEST_FILE = "../data/test.txt"
OUTPUT_FILE = f"../bin/model{now}.csv"

def main():
    classifier = ft.load_model(MODEL_FILE)
    with open(TEST_FILE, 'r') as fin:
        qlite = fin.readlines()

    tagger = MeCab.Tagger('-Owakati')
    output_csv = []
    for q in qlite:
        line = tagger.parse(q)
        labels, probs = classifier.predict(line.strip(), k=2)
        output = []
        for label, prob in zip(labels, probs):
            output.append(re.sub("__label__", "", label) + ":" + str(prob))
        output.append(q.strip())
        output_csv.append(",".join(output))
    with open(OUTPUT_FILE, "wt") as fout:
        fout.write("\n".join(output_csv))

if __name__ == '__main__':
    main()
