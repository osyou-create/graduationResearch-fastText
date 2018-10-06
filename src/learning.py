import sys
import fastText as ft

argvs = sys.argv
#input_file = argvs[1]


classifier = ft.train_supervised(f"../data/model02.txt")
classifier.save_model(f'../bin/model02.bin')
