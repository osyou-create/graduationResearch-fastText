import random

INPUT_FILE="yes.txt"
OUTPUT_FILE="test01.txt"

def main():
    f=open(f"../data/{INPUT_FILE}","r")
    l=f.readlines()

    s=random.sample(l,20)

    with open(f"../data/{OUTPUT_FILE}", "wt") as fout:
        fout.write("".join(s))


if __name__=="__main__":
    main()