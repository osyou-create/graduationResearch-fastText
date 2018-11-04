import sys
import fastText as ft
import MeCab
import re
import datetime

name = "test01"

MODEL_FILE = "../bin/model1007_0003.bin"
TEST_FILE = f"../data/{name}.txt"
OUTPUT_FILE = f"../bin/{name}.csv"

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
