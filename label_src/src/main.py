import sys

PATH = '../data/'
fileName = ""

def writing(text):
    """
    ファイルに書き込み
    """
    with open(f"{PATH}la_{fileName}.txt",'a') as t:
        t.write(text)

def judge(text):
    """
    一目で判断して、書き込むか否かを判断する。
    """
    print(text)
    print('Q.この文章は皮肉ですか？')
    tmp = input('(yes:1/no:2) >>')
    tmp = int(tmp)
    if tmp == 1:
        wt = label(text)
        writing(wt)
        print(f'{text}を書き込みました。')
        print('--------------------')
    elif tmp == 2:
        print(f'{text}は書き込まれませんでした。')
        print('--------------------')
    else:
        print('1 or 2で入力してください。スキップします。')
        print('--------------------')


def label(text):
    """
    行の先頭にlabelを付けて送り返す
    """
    labelName = '携帯' #ラベル付けをしたい名前を入力する

    sendLabel = f'__label__{labelName},'
    return f'{sendLabel} {text}'

def tweet():
    """
    tweetを一行ずつ取得
    """
    f = open(f"{PATH}{fileName}.txt",'r')

    tweet = f.readline()
    while tweet:
        judge(tweet)
        label(tweet)
        tweet = f.readline()
    f.close()

if __name__ == '__main__':
    fileName = input("読み込むファイル名を入力してください　>>")
    tweet()
