import requests
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

porter = PorterStemmer()
stop_words = stopwords.words('english')
r = requests.get("https://httpstatuses.com/")
l = re.findall('<li><a href="/(.*?)"><span>(.*?)</span> (.*?)</a></li>', r.text)
l = [i[2].split(' ') for i in l]
cleared_list = []
for i in l:
    for j in i:
        if j.lower() not in stop_words:
            cleared_list.append(j)
final_list = [cleared_list[0]]
for i in cleared_list:
    if porter.stem(i) not in [porter.stem(word) for word in final_list]:
        final_list.append(i)
print(final_list)


