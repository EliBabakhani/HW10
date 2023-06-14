import requests
import json

count = 0


def get_res(url: str):
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()  # create a list of json obj
        return data
    else:
        return None


def process(data: json):
    posts = []
    for record in data:
        posts.append(record["id"])
    return len(posts)


def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = get_res(url)
    data_final = process(data)
    global count
    num_process = count

    def inner(n):
        nonlocal num_process
        num_process += n

    inner(data_final)
    record_process = num_process
    print(f"record number is: {record_process}")


if __name__ == "__main__":
    main()
