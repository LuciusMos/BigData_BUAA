# import jieba
import pandas as pd

txt = '你的回答一定要让招生官觉得你是因为有妥善规划、所以才没有应届申请，而不是因为你考分能力不行。比如你可以回答你是因为想先工作积累经验再申请，或者是因为你工作之后发现自己需要更多的专业知识所以想读研。如果题主还有什么想要了解自己除了语言成绩还适合做哪方面的提升，欢迎私信我或加我微信'
print(jieba.lcut(txt))


train = pd.read_csv('train.csv')
train.info()