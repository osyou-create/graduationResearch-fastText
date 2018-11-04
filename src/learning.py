import sys
import fastText as ft
import datetime

INPUT_FILE = "hiniku_input01"
TEST_FILE = "test02"

def print_result(N, p, r):
    print("N\t" + str(N))
    print("P@{}\t{:.3f}".format(1, p))
    print("R@{}\t{:.3f}".format(1, r))

def main():
    train_data = f"../data/{INPUT_FILE}.txt"
    valid_data = f"../data/{TEST_FILE}.txt"
    now = datetime.datetime.today().strftime("%m%d_%H%M")

    model = ft.train_supervised(input=train_data,epoch=1000,loss="hs")
    print_result(*model.test(valid_data))
    model.save_model(f"../bin/model{now}.bin")

if __name__ == "__main__":
    main()
