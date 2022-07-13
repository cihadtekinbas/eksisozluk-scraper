import json

f = open('datalast.json')

data = json.load(f)
f.close()
print(len(data['data']))
import time
import datetime
from eksisozluk.EksiSozluk import EksiApi
client=EksiApi()


temp=[]
skip=False
fail=False
for i in data['data']: 
    dataset={}
    dataset['id']=i['id']
    dataset['title']=i['title']
    dataset['slug']=i['slug']
    dataset['total_page']=i['total_page']
    entris_l=[]    
    for j in range(1,i['total_page']):
        try:
            fail=False
            topic = client.get_topic(int(i['id']),j)
            for z in topic.topic.entries:
                entr={}    
                entr['id']=z.id
                entr['content']=z.content
                entr['created']=z.created.strftime("%m/%d/%Y, %H:%M:%S")

                entr['favorite_count']=z.favorite_count
                entr['author_id']=z.author.id
                entr['author_id']=z.author.id
                entris_l.append(entr)

        except Exception as identifier:
            print(identifier,"fail")
            fail=True
            pass
    if fail==False:
        dataset['entry_count']=len(entris_l)

        dataset['entries']=entris_l
        temp.append(dataset)

    
        
        
w={}
w['data']=temp
with open('templast_last_last.json', 'w') as s:
    json.dump(w, s, ensure_ascii=False,indent=4)



