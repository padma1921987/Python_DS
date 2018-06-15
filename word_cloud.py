import collections
file = open("C:\\Users\\SONY\\Desktop\\fashion.txt","r")
file2=open("C:\\Users\\SONY\\Desktop\\data science in python\\word_cloud_assignment\\stopwords","r")
wordcount={}
wordcount2={}
for j in (file2.read().lower().split()):
    for i in (file.read().lower().split()):
        i = i.replace(".", "")
        i = i.replace(",", "")
        i = i.replace("\"", "")
        i = i.replace("“", "")
       # i = i.replace("'","")
        if j != i:
            if i not in wordcount:
                wordcount[i]=1
            else:
                wordcount[i]=wordcount[i]+1
print('{:15}{:3}'.format('word','count'))
print('_'*18)
#for key in sorted(wordcount,key=wordcount.get,reverse=True):
for word,count in (collections.Counter(wordcount)).most_common(5):
        print('{:15}{:3}'.format(word,count))

