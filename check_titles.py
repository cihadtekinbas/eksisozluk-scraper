import json
import requests as r
f = open('result.json')
data = json.load(f)

temp=[]
skip=False
count=0
for i in data['messages']:

    try:
        entry=i['text'][0][:-1].lower()

        if skip:

            req = r.get("http://localhost:3000/api/baslik/"+entry)
            d=req.json()
            dataset={}

            if False==('error' in d):
                dataset['entry']=entry
                dataset['id']=d['id']
                dataset['title']=d['title']
                dataset['slug']=d['slug']
                dataset['total_page']=d['total_page']
                temp.append(dataset)
                count+=1
        if entry=="kafelerde isıtıcının ücretli olması":
            skip=True
        
    except Exception as e:
        print(i)
        print(e)
        
        pass
    
    if count%100==0:
        print(count)

    


            
print(count)     
w={}
w['data']=temp
with open('data3.json', 'w') as s:
    json.dump(w, s, ensure_ascii=False,indent=4)
s.close()
f.close()