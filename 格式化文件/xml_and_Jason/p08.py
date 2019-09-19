# 案例08
import json

data = {"name":"hahah", "age":12}

'''
with open("t.json", 'w') as f:
    json.dump(data, f)
'''
with open("loss.json", 'r') as f:
    d = json.load(f)
    print(type(d))
    print(d)
    print(d['Loss'])
    gps = d['Loss']['GPS']
    gsm = d['Loss']['GSM']
    print(type(gsm))
    print(gsm)
    print(len(gsm))
    for i in gsm:
        print(i)