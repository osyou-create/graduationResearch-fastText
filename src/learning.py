import sys
import fastText as ft
import datetime

now = datetime.datetime.today().strftime("%m%d_%H%M")

INPUT_FILE = "hiniku_input01.txt"
OUTPUT_FILE = f"../bin/model{now}.txt"

argvs = sys.argv
#input_file = argvs[1]

classifier = ft.train_supervised(f"../data/{INPUT_FILE}")
classifier.save_model(OUTPUT_FILE)
