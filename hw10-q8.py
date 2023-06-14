import requests
import json

count = 0


def get_res(url: str):
    global count
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()  # create a list of json obj
        return data
    else:
        return []


def process(data: json):
    global count
    count = 0
    for record in data:
        count += 1
    print(count)


def outer(): #??????????
    c=0
    def inner():
        nonlocal c
        c+=1
        print(c)
    return inner()

# outer()



# print(show())
# with open('data.json','w') as handle:
#     json.dump(datam,handle)
# with open('data.json','r') as p:
#     print(json.load([0]))
a=get_res('https://jsonplaceholder.typicode.com/posts')
b=process(a)

