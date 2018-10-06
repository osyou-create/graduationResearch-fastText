TEXT_PATH = "../data/"

def tweet():
    fileName = "phone03"
    fr = open(f"{TEXT_PATH}{fileName}.txt",'r')
    tweet = fr.readline()
    while tweet:
        with open(f"../../fastText/data/{fileName}.txt",'a')as tw:
            tw.write(f"__label__携帯, {tweet}")
        tweet = fr.readline()

if __name__ == '__main__':
    tweet()
