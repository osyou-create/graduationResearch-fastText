import sys
import fastText as ft
import MeCab

class predict:
    def __init__(self):
        self.classifier = ft.load_model('../bin/model02.bin')

    def get_surfaces(self, content):
        """
        文書を分かち書き
        """
        tagger = MeCab.Tagger('')
        tagger.parse('')
        surfaces = []
        node = tagger.parseToNode(content)

        while node:
            surfaces.append(node.surface)
            node = node.next

        return surfaces


    def tweet_class(self, content):
        """
        ツイートを解析して分類を行う
        """
        words = " ".join(self.get_surfaces(content))
        print(words)
        date = self.classifier.predict(text=words,k=3)
        print(date)


if __name__ == '__main__':
    pre = predict()
    file = open('../data/la_phone.txt','r')
    tweet = file.readline()
    while tweet:
        pre.tweet_class(tweet)
        tweet = file.readline()
