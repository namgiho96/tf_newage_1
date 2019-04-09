from konlpy.tag import Okt
import pandas as pd
# import nltk
# nltk.download()

from nltk.tokenize import word_tokenize
from nltk import  FreqDist
import  re
from wordcloud import WordCloud
import matplotlib.pyplot as plt  # 그래프 그려주는거

okt = Okt()
ctx = '../data/'
filename = ctx+'kr-Report_2018.txt'
stopword = ctx+'stopwords.txt'

with open(filename, 'r', encoding='utf-8') as f:  # 'r'은 리드 온리이다 읽기만 가능한 상태를
    texts = f.read()


texts = texts.replace('\n', '')
tokenizer = re.compile(r'[^ ㄱ-힣]+')  # 한글과 제외한 모든글자
texts = tokenizer.sub('', texts)
# print(texts[:300])   # 300번째 까지 표출하라고 하는거다

tokens = word_tokenize(texts)

noun_tokens = []
for t in tokens:
    t_pos = okt.pos(t)
    t2 = [i[0] for i in t_pos
          if i[1] == 'Noun']
    if len("".join(t2)) > 1:
        noun_tokens.append("".join(t2))
texts = " ".join(noun_tokens)
# print(texts[:300])

with open(stopword, 'r', encoding='utf-8') as f:
    stopword = f.read()


# print(stopwords[:300])
stopwords = stopword.split(' ')
texts = [text for text in tokens if text not in stopword]
freqtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)


okt.pos('가치창춤')
okt.pos('갤럭시')

wcloud = WordCloud(ctx+'D2Coding.ttf', relative_scaling=0.2
                   , background_color='white').generate(" ".join(texts))

plt.figure(figsize=(12,12))
plt.imshow(wcloud, interpolation='bilinear')
plt.show()




